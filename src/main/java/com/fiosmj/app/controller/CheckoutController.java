package com.fiosmj.app.controller;

import com.fiosmj.app.model.CheckoutRequest;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.*;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/api/checkout")
public class CheckoutController {

    @Value("${mercadopago.access-token}")
    private String accessToken;

    private final RestTemplate restTemplate = new RestTemplate();

    @PostMapping("/preference")
    public ResponseEntity<?> createPreference(@RequestBody CheckoutRequest req) {
        try {
            // Build items list for MP
            List<Map<String, Object>> mpItems = req.getItems().stream().map(item -> {
                Map<String, Object> mpItem = new LinkedHashMap<>();
                mpItem.put("title", item.getProductName() != null ? item.getProductName() : "Produto Fios MJ");
                mpItem.put("quantity", item.getQuantity() != null ? item.getQuantity() : 1);
                mpItem.put("unit_price", item.getPrice() != null ? item.getPrice() : 0.0);
                mpItem.put("currency_id", "BRL");
                return mpItem;
            }).collect(Collectors.toList());

            // Build payer info
            Map<String, Object> mpPayer = new LinkedHashMap<>();
            if (req.getPayer() != null) {
                mpPayer.put("name", req.getPayer().getName() != null ? req.getPayer().getName() : "");
                String email = (req.getPayer().getEmail() != null && !req.getPayer().getEmail().isBlank())
                    ? req.getPayer().getEmail()
                    : "cliente@fiosmj.com";
                mpPayer.put("email", email);
            } else {
                mpPayer.put("email", "cliente@fiosmj.com");
            }

            // Build back_urls
            Map<String, String> backUrls = new LinkedHashMap<>();
            backUrls.put("success", "https://fiosmj.com/obrigado");
            backUrls.put("failure", "https://fiosmj.com");
            backUrls.put("pending", "https://fiosmj.com/pendente");

            // Build request body
            Map<String, Object> body = new LinkedHashMap<>();
            body.put("items", mpItems);
            body.put("payer", mpPayer);
            body.put("back_urls", backUrls);
            body.put("auto_return", "approved");

            // Set headers
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);
            headers.set("Authorization", "Bearer " + accessToken);

            HttpEntity<Map<String, Object>> entity = new HttpEntity<>(body, headers);

            ResponseEntity<Map> response = restTemplate.exchange(
                "https://api.mercadopago.com/checkout/preferences",
                HttpMethod.POST,
                entity,
                Map.class
            );

            Map<?, ?> mpBody = response.getBody();
            if (mpBody == null) {
                return ResponseEntity.status(HttpStatus.BAD_GATEWAY)
                    .body(Map.of("error", "Empty response from Mercado Pago"));
            }

            Map<String, Object> result = new LinkedHashMap<>();
            result.put("init_point", mpBody.get("init_point"));
            result.put("preference_id", mpBody.get("id"));

            return ResponseEntity.ok(result);

        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body(Map.of("error", e.getMessage()));
        }
    }
}
