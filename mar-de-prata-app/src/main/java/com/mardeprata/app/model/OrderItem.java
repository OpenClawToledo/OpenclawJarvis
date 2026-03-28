package com.mardeprata.app.model;

import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;

@Entity
@Table(name = "order_items")
public class OrderItem {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "order_id")
    @JsonIgnore
    private TableOrder order;

    @ManyToOne
    @JoinColumn(name = "menu_item_id")
    private MenuItem menuItem;

    private Integer quantity;
    private Double unitPrice;
    private String notes; // ex: "sem pimenta", "extra molho"

    // Getters e Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public TableOrder getOrder() { return order; }
    public void setOrder(TableOrder order) { this.order = order; }
    public MenuItem getMenuItem() { return menuItem; }
    public void setMenuItem(MenuItem menuItem) { this.menuItem = menuItem; }
    public Integer getQuantity() { return quantity; }
    public void setQuantity(Integer quantity) { this.quantity = quantity; }
    public Double getUnitPrice() { return unitPrice; }
    public void setUnitPrice(Double unitPrice) { this.unitPrice = unitPrice; }
    public String getNotes() { return notes; }
    public void setNotes(String notes) { this.notes = notes; }
}
