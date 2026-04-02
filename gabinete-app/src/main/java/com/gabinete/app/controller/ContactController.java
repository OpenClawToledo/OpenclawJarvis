package com.gabinete.app.controller;

import com.gabinete.app.config.AdminSecretValidator;
import com.gabinete.app.model.ContactMessage;
import com.gabinete.app.repository.ContactMessageRepository;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/contact")
public class ContactController {

    @Autowired private ContactMessageRepository contactMessageRepository;
    @Autowired private AdminSecretValidator adminSecret;

    // POST /api/contact — formulário público
    @PostMapping
    public ResponseEntity<?> submitContact(@Valid @RequestBody ContactMessage message) {
        try {
            contactMessageRepository.save(message);
            return ResponseEntity.ok(Map.of(
                "success", true,
                "message", "Mensagem recebida. Entraremos em contacto brevemente."
            ));
        } catch (Exception e) {
            // Nunca expor detalhes internos
            return ResponseEntity.internalServerError()
                .body(Map.of("error", "Erro interno. Tente novamente."));
        }
    }

    // GET /api/contact — admin: listar mensagens
    @GetMapping
    public ResponseEntity<?> getMessages(
            @RequestHeader(value = "X-Admin-Secret", required = false) String secret) {
        if (!adminSecret.isValid(secret))
            return ResponseEntity.status(403).body(Map.of("error", "Acesso negado"));
        return ResponseEntity.ok(contactMessageRepository.findAllByOrderByCreatedAtDesc());
    }

    // PUT /api/contact/{id}/read — admin: marcar como lida
    @PutMapping("/{id}/read")
    public ResponseEntity<?> markRead(
            @PathVariable Long id,
            @RequestHeader(value = "X-Admin-Secret", required = false) String secret) {
        if (!adminSecret.isValid(secret))
            return ResponseEntity.status(403).body(Map.of("error", "Acesso negado"));
        return contactMessageRepository.findById(id).map(msg -> {
            msg.setRead(true);
            contactMessageRepository.save(msg);
            return ResponseEntity.ok(Map.of("success", true));
        }).orElse(ResponseEntity.notFound().build());
    }
}
