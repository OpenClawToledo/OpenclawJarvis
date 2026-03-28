package com.gabinete.app.controller;

import com.gabinete.app.model.ContactMessage;
import com.gabinete.app.repository.ContactMessageRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/contact")
public class ContactController {

    @Autowired
    private ContactMessageRepository contactMessageRepository;

    // POST /api/contact — formulário de contacto
    @PostMapping
    public ResponseEntity<?> submitContact(@RequestBody ContactMessage message) {
        try {
            ContactMessage saved = contactMessageRepository.save(message);
            return ResponseEntity.ok(Map.of(
                "success", true,
                "message", "Mensagem recebida. Entraremos em contacto brevemente."
            ));
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    // GET /api/contact (admin) — listar mensagens
    @GetMapping
    public ResponseEntity<List<ContactMessage>> getMessages(
            @RequestHeader("X-Admin-Secret") String secret) {
        String adminSecret = System.getenv().getOrDefault("ADMIN_SECRET", "gabinete-admin-secret");
        if (!adminSecret.equals(secret)) {
            return ResponseEntity.status(403).build();
        }
        return ResponseEntity.ok(contactMessageRepository.findAllByOrderByCreatedAtDesc());
    }

    // PUT /api/contact/{id}/read (admin)
    @PutMapping("/{id}/read")
    public ResponseEntity<?> markRead(
            @PathVariable Long id,
            @RequestHeader("X-Admin-Secret") String secret) {
        String adminSecret = System.getenv().getOrDefault("ADMIN_SECRET", "gabinete-admin-secret");
        if (!adminSecret.equals(secret)) {
            return ResponseEntity.status(403).build();
        }
        return contactMessageRepository.findById(id).map(msg -> {
            msg.setRead(true);
            contactMessageRepository.save(msg);
            return ResponseEntity.ok(Map.of("success", true));
        }).orElse(ResponseEntity.notFound().build());
    }
}
