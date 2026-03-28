package com.gabinete.app.controller;

import com.gabinete.app.model.Service;
import com.gabinete.app.repository.ServiceRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/services")
public class ServiceController {

    @Autowired
    private ServiceRepository serviceRepository;

    // GET /api/services — lista de serviços activos
    @GetMapping
    public ResponseEntity<List<Service>> getServices() {
        return ResponseEntity.ok(serviceRepository.findByActiveTrueOrderByDisplayOrderAsc());
    }

    // POST /api/services (admin) — criar serviço
    @PostMapping
    public ResponseEntity<?> createService(
            @RequestBody Service service,
            @RequestHeader("X-Admin-Secret") String secret) {
        String adminSecret = System.getenv().getOrDefault("ADMIN_SECRET", "gabinete-admin-secret");
        if (!adminSecret.equals(secret)) return ResponseEntity.status(403).build();
        return ResponseEntity.ok(serviceRepository.save(service));
    }

    // PUT /api/services/{id} (admin) — editar serviço
    @PutMapping("/{id}")
    public ResponseEntity<?> updateService(
            @PathVariable Long id,
            @RequestBody Service updated,
            @RequestHeader("X-Admin-Secret") String secret) {
        String adminSecret = System.getenv().getOrDefault("ADMIN_SECRET", "gabinete-admin-secret");
        if (!adminSecret.equals(secret)) return ResponseEntity.status(403).build();
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
