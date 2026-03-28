package com.gabinete.app.model;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "contact_messages")
public class ContactMessage {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false)
    private String email;

    private String phone;
    private String company;

    @Column(columnDefinition = "TEXT", nullable = false)
    private String message;

    private String service; // qual serviço tem interesse
    private String lang = "pt"; // pt ou zh

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
    public void setName(String name) { this.name = name; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public String getCompany() { return company; }
    public void setCompany(String company) { this.company = company; }
    public String getMessage() { return message; }
    public void setMessage(String message) { this.message = message; }
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
