package com.gabinete.app.model;

import jakarta.persistence.*;
import jakarta.validation.constraints.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "contact_messages")
public class ContactMessage {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotBlank(message = "Nome obrigatório")
    @Size(max = 120, message = "Nome demasiado longo")
    @Column(nullable = false)
    private String name;

    @NotBlank(message = "Email obrigatório")
    @Email(message = "Email inválido")
    @Size(max = 200, message = "Email demasiado longo")
    @Column(nullable = false)
    private String email;

    @Size(max = 30, message = "Telefone demasiado longo")
    @Pattern(regexp = "^[+\\d\\s\\-()]*$", message = "Telefone inválido")
    private String phone;

    @Size(max = 150, message = "Empresa demasiado longa")
    private String company;

    @NotBlank(message = "Mensagem obrigatória")
    @Size(min = 10, max = 2000, message = "Mensagem entre 10 e 2000 caracteres")
    @Column(columnDefinition = "TEXT", nullable = false)
    private String message;

    @Size(max = 80)
    private String service;

    @Pattern(regexp = "^(pt|zh|en)$", message = "Idioma inválido")
    private String lang = "pt";

    private Boolean read = false;
    private Boolean replied = false;

    @Column(name = "created_at")
    private LocalDateTime createdAt;

    @PrePersist
    protected void onCreate() { createdAt = LocalDateTime.now(); }

    // Getters e Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name != null ? name.strip() : null; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email != null ? email.strip().toLowerCase() : null; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public String getCompany() { return company; }
    public void setCompany(String company) { this.company = company != null ? company.strip() : null; }
    public String getMessage() { return message; }
    public void setMessage(String message) { this.message = message != null ? message.strip() : null; }
    public String getService() { return service; }
    public void setService(String service) { this.service = service; }
    public String getLang() { return lang; }
    public void setLang(String lang) { this.lang = lang; }
    public Boolean getRead() { return read; }
    public void setRead(Boolean read) { this.read = read; }
    public Boolean getReplied() { return replied; }
    public void setReplied(Boolean replied) { this.replied = replied; }
    public LocalDateTime getCreatedAt() { return createdAt; }
}
