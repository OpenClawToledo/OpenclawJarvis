package com.gabinete.app.controller;

import com.gabinete.app.config.AdminSecretValidator;
import com.gabinete.app.model.Service;
import com.gabinete.app.repository.ServiceRepository;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/services")
public class ServiceController {

    @Autowired private ServiceRepository serviceRepository;
    @Autowired private AdminSecretValidator adminSecret;

    // GET /api/services — público
    @GetMapping
    public ResponseEntity<List<Service>> getServices() {
        return ResponseEntity.ok(serviceRepository.findByActiveTrueOrderByDisplayOrderAsc());
    }

    // POST /api/services — admin
    @PostMapping
    public ResponseEntity<?> createService(
            @Valid @RequestBody Service service,
            @RequestHeader(value = "X-Admin-Secret", required = false) String secret) {
        if (!adminSecret.isValid(secret))
            return ResponseEntity.status(403).body(Map.of("error", "Acesso negado"));
        return ResponseEntity.ok(serviceRepository.save(service));
    }

    // PUT /api/services/{id} — admin
    @PutMapping("/{id}")
    public ResponseEntity<?> updateService(
            @PathVariable Long id,
            @Valid @RequestBody Service updated,
            @RequestHeader(value = "X-Admin-Secret", required = false) String secret) {
        if (!adminSecret.isValid(secret))
            return ResponseEntity.status(403).body(Map.of("error", "Acesso negado"));
        return serviceRepository.findById(id).map(s -> {
            s.setNamePt(updated.getNamePt());
            s.setNameZh(updated.getNameZh());
            s.setDescriptionPt(updated.getDescriptionPt());
            s.setDescriptionZh(updated.getDescriptionZh());
            s.setIcon(updated.getIcon());
            s.setActive(updated.getActive());
            s.setDisplayOrder(updated.getDisplayOrder());
            return ResponseEntity.ok(serviceRepository.save(s));
        }).orElse(ResponseEntity.notFound().build());
    }
}
