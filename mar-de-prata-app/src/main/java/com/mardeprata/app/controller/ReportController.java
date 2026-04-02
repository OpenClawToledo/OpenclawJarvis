package com.mardeprata.app.controller;

import com.mardeprata.app.model.TableOrder;
import com.mardeprata.app.repository.TableOrderRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDateTime;
import java.util.*;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/api/reports")
public class ReportController {

    @Autowired
    private TableOrderRepository orderRepository;

    @GetMapping
    public ResponseEntity<?> getReport(
            @RequestParam(defaultValue = "day") String period,
            @RequestHeader("X-Admin-Secret") String secret) {

        String adminSecret = System.getenv().getOrDefault("ADMIN_SECRET", "mar-de-prata-admin-secret");
        if (!adminSecret.equals(secret)) {
            return ResponseEntity.status(403).body(Map.of("error", "Acesso negado"));
        }

        LocalDateTime start;
        LocalDateTime now = LocalDateTime.now();
        switch (period) {
            case "week": start = now.minusWeeks(1); break;
            case "month": start = now.minusMonths(1); break;
            default: start = now.toLocalDate().atStartOfDay(); break;
        }

        List<TableOrder> orders = orderRepository.findByCreatedAtAfterOrderByCreatedAtDesc(start);

        double totalRevenue = orders.stream()
            .filter(o -> o.getStatus() != TableOrder.Status.CANCELLED)
            .mapToDouble(TableOrder::getTotalPrice).sum();

        long served = orders.stream().filter(o -> o.getStatus() == TableOrder.Status.SERVED).count();
        long cancelled = orders.stream().filter(o -> o.getStatus() == TableOrder.Status.CANCELLED).count();
        long inProgress = orders.size() - served - cancelled;

        // Top 5 pratos mais pedidos
        Map<String, Long> itemCounts = new HashMap<>();
        Map<String, Double> itemRevenue = new HashMap<>();
        orders.stream()
            .filter(o -> o.getStatus() != TableOrder.Status.CANCELLED)
            .flatMap(o -> o.getItems().stream())
            .forEach(item -> {
                String name = item.getMenuItem().getName();
                itemCounts.merge(name, (long) item.getQuantity(), Long::sum);
                itemRevenue.merge(name, item.getUnitPrice() * item.getQuantity(), Double::sum);
            });

        List<Map<String, Object>> top5 = itemCounts.entrySet().stream()
            .sorted(Map.Entry.<String, Long>comparingByValue().reversed())
            .limit(5)
            .map(e -> {
                Map<String, Object> m = new LinkedHashMap<>();
                m.put("name", e.getKey());
                m.put("quantity", e.getValue());
                m.put("revenue", itemRevenue.getOrDefault(e.getKey(), 0.0));
                return m;
            })
            .collect(Collectors.toList());

        long nonCancelledCount = orders.stream()
            .filter(o -> o.getStatus() != TableOrder.Status.CANCELLED).count();
        double avgOrder = nonCancelledCount == 0 ? 0 : totalRevenue / nonCancelledCount;

        Map<String, Object> result = new LinkedHashMap<>();
        result.put("period", period);
        result.put("totalOrders", orders.size());
        result.put("totalRevenue", Math.round(totalRevenue * 100.0) / 100.0);
        result.put("served", served);
        result.put("cancelled", cancelled);
        result.put("inProgress", inProgress);
        result.put("avgOrderValue", Math.round(avgOrder * 100.0) / 100.0);
        result.put("top5Items", top5);

        return ResponseEntity.ok(result);
    }
}
