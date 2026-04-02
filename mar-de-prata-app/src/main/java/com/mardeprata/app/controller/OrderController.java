package com.mardeprata.app.controller;

import com.mardeprata.app.model.MenuItem;
import com.mardeprata.app.model.OrderItem;
import com.mardeprata.app.model.TableOrder;
import com.mardeprata.app.repository.MenuItemRepository;
import com.mardeprata.app.repository.TableOrderRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/api/orders")
public class OrderController {

    @Autowired
    private TableOrderRepository orderRepository;

    @Autowired
    private MenuItemRepository menuItemRepository;

    @Autowired
    private SimpMessagingTemplate messagingTemplate;

    // POST /api/orders — cliente faz pedido da mesa
    @PostMapping
    public ResponseEntity<?> createOrder(@RequestBody Map<String, Object> body) {
        try {
            Integer tableNumber = (Integer) body.get("tableNumber");
            String notes = (String) body.getOrDefault("notes", "");
            List<Map<String, Object>> itemsData = (List<Map<String, Object>>) body.get("items");

            if (tableNumber == null || itemsData == null || itemsData.isEmpty()) {
                return ResponseEntity.badRequest().body(Map.of("error", "Mesa e itens são obrigatórios"));
            }

            TableOrder order = new TableOrder();
            order.setTableNumber(tableNumber);
            order.setNotes(notes);

            double total = 0.0;
            for (Map<String, Object> itemData : itemsData) {
                Long menuItemId = Long.valueOf(itemData.get("menuItemId").toString());
                Integer quantity = Integer.valueOf(itemData.get("quantity").toString());
                String itemNotes = (String) itemData.getOrDefault("notes", "");

                MenuItem menuItem = menuItemRepository.findById(menuItemId).orElse(null);
                if (menuItem == null) continue;

                OrderItem orderItem = new OrderItem();
                orderItem.setOrder(order);
                orderItem.setMenuItem(menuItem);
                orderItem.setQuantity(quantity);
                orderItem.setUnitPrice(menuItem.getPrice());
                orderItem.setNotes(itemNotes);

                total += menuItem.getPrice() * quantity;
            }

            order.setTotalPrice(total);
            TableOrder saved = orderRepository.save(order);

            // Notificar cozinha via WebSocket
            messagingTemplate.convertAndSend("/topic/kitchen", saved);

            return ResponseEntity.ok(Map.of(
                "success", true,
                "orderId", saved.getId(),
                "tableNumber", saved.getTableNumber(),
                "total", saved.getTotalPrice(),
                "status", saved.getStatus()
            ));
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    // GET /api/orders — todos os pedidos activos (para cozinha e painel ADM)
    @GetMapping
    public ResponseEntity<?> getAllOrders(@RequestHeader(value = "X-Admin-Secret", required = false) String secret) {
        String adminSecret = System.getenv().getOrDefault("ADMIN_SECRET", "mar-de-prata-admin-secret");
        if (secret == null || !adminSecret.equals(secret)) {
            return ResponseEntity.status(403).body(Map.of("error", "Acesso negado"));
        }
        // Retorna todos exceto CANCELLED, ordenados do mais recente
        List<TableOrder> all = orderRepository.findAllByOrderByCreatedAtDesc().stream()
                .filter(o -> o.getStatus() != TableOrder.Status.CANCELLED)
                .collect(Collectors.toList());
        return ResponseEntity.ok(all);
    }

    // GET /api/orders/table/{tableNumber} — pedidos activos de uma mesa
    @GetMapping("/table/{tableNumber}")
    public ResponseEntity<List<TableOrder>> getTableOrders(@PathVariable Integer tableNumber) {
        return ResponseEntity.ok(orderRepository.findByTableNumberOrderByCreatedAtDesc(tableNumber));
    }

    // GET /api/orders/pending — pedidos pendentes (para cozinha)
    @GetMapping("/pending")
    public ResponseEntity<List<TableOrder>> getPendingOrders() {
        return ResponseEntity.ok(orderRepository.findByStatusOrderByCreatedAtDesc(TableOrder.Status.PENDING));
    }

    // PUT /api/orders/{id}/status — cozinha atualiza estado
    @PutMapping("/{id}/status")
    public ResponseEntity<?> updateStatus(
            @PathVariable Long id,
            @RequestBody Map<String, String> body,
            @RequestHeader("X-Admin-Secret") String secret) {

        String adminSecret = System.getenv().getOrDefault("ADMIN_SECRET", "mar-de-prata-admin-secret");
        if (!adminSecret.equals(secret)) {
            return ResponseEntity.status(403).body(Map.of("error", "Acesso negado"));
        }

        return orderRepository.findById(id).map(order -> {
            TableOrder.Status status = TableOrder.Status.valueOf(body.get("status"));
            order.setStatus(status);
            TableOrder updated = orderRepository.save(order);
            // Notificar via WebSocket
            messagingTemplate.convertAndSend("/topic/kitchen", updated);
            messagingTemplate.convertAndSend("/topic/table/" + updated.getTableNumber(), updated);
            return ResponseEntity.ok(updated);
        }).orElse(ResponseEntity.notFound().build());
    }
}
