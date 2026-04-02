package com.gabinete.app.config;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.security.MessageDigest;
import java.nio.charset.StandardCharsets;

/**
 * Validador centralizado do segredo de admin.
 * Usa comparação timing-safe para prevenir timing attacks.
 */
@Component
public class AdminSecretValidator {

    @Value("${app.admin-secret}")
    private String adminSecret;

    /**
     * Compara o segredo recebido com o segredo configurado.
     * Timing-safe: tempo constante independentemente do resultado.
     */
    public boolean isValid(String provided) {
        if (provided == null || adminSecret == null) return false;
        byte[] a = provided.getBytes(StandardCharsets.UTF_8);
        byte[] b = adminSecret.getBytes(StandardCharsets.UTF_8);
        return MessageDigest.isEqual(a, b);
    }
}
