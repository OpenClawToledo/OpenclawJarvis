package com.mardeprata.app.model;

import jakarta.persistence.*;
import java.time.LocalDateTime;
import java.util.List;

@Entity
@Table(name = "table_orders")
public class TableOrder {

    public enum Status {
        PENDING,    // Pedido chegou, aguarda confirmação
        CONFIRMED,  // Confirmado pela cozinha
        PREPARING,  // Em preparação
        READY,      // Pronto para servir
        SERVED,     // Servido
        CANCELLED   // Cancelado
    }

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "table_number", nullable = false)
    private Integer tableNumber;

    @Enumerated(EnumType.STRING)
    private Status status = Status.PENDING;

    private String notes; // Observações do cliente

    @Column(name = "total_price")
    private Double totalPrice = 0.0;

    @OneToMany(mappedBy = "order", cascade = CascadeType.ALL, fetch = FetchType.EAGER)
    private List<OrderItem> items;

    @Column(name = "created_at")
    private LocalDateTime createdAt;

    @Column(name = "updated_at")
    private LocalDateTime updatedAt;

    @PrePersist
    protected void onCreate() {
        createdAt = LocalDateTime.now();
        updatedAt = LocalDateTime.now();
    }

    @PreUpdate
    protected void onUpdate() {
        updatedAt = LocalDateTime.now();
    }

    // Getters e Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public Integer getTableNumber() { return tableNumber; }
    public void setTableNumber(Integer tableNumber) { this.tableNumber = tableNumber; }
    public Status getStatus() { return status; }
    public void setStatus(Status status) { this.status = status; }
    public String getNotes() { return notes; }
    public void setNotes(String notes) { this.notes = notes; }
    public Double getTotalPrice() { return totalPrice; }
    public void setTotalPrice(Double totalPrice) { this.totalPrice = totalPrice; }
    public List<OrderItem> getItems() { return items; }
    public void setItems(List<OrderItem> items) { this.items = items; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public LocalDateTime getUpdatedAt() { return updatedAt; }
}
