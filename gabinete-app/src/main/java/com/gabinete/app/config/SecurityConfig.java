package com.gabinete.app.config;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpMethod;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.header.writers.ReferrerPolicyHeaderWriter;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.CorsConfigurationSource;
import org.springframework.web.cors.UrlBasedCorsConfigurationSource;

import java.util.List;

@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Value("${app.base-url:http://localhost:8084}")
    private String baseUrl;

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            // Sem CSRF — API stateless
            .csrf(csrf -> csrf.disable())

            // CORS — só aceita a própria origem
            .cors(cors -> cors.configurationSource(corsConfigurationSource()))

            // Sem sessão
            .sessionManagement(sm -> sm
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS))

            // Security headers
            .headers(headers -> headers
                .frameOptions(fo -> fo.deny())
                .contentTypeOptions(ct -> {})
                .httpStrictTransportSecurity(hsts -> hsts
                    .maxAgeInSeconds(31536000)
                    .includeSubDomains(true))
                .referrerPolicy(rp -> rp
                    .policy(ReferrerPolicyHeaderWriter.ReferrerPolicy.STRICT_ORIGIN_WHEN_CROSS_ORIGIN))
            )

            // Autorização por endpoint
            .authorizeHttpRequests(auth -> auth
                // Frontend
                .requestMatchers("/", "/index.html", "/assets/**", "/uploads/**").permitAll()
                // API pública
                .requestMatchers(HttpMethod.GET,  "/api/services").permitAll()
                .requestMatchers(HttpMethod.POST, "/api/contact").permitAll()
                // Admin — autenticação feita no controller via X-Admin-Secret timing-safe
                .requestMatchers("/api/contact/**", "/api/services/**", "/api/admin/**").permitAll()
                // Tudo o resto bloqueado
                .anyRequest().denyAll()
            );

        return http.build();
    }

    @Bean
    public CorsConfigurationSource corsConfigurationSource() {
        CorsConfiguration config = new CorsConfiguration();
        // Só aceita requests da própria origem do site
        config.setAllowedOrigins(List.of(baseUrl));
        config.setAllowedMethods(List.of("GET", "POST", "PUT", "DELETE", "OPTIONS"));
        config.setAllowedHeaders(List.of("Content-Type", "X-Admin-Secret", "Authorization"));
        config.setAllowCredentials(false);
        config.setMaxAge(3600L);

        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
        source.registerCorsConfiguration("/api/**", config);
        return source;
    }
}
