package com.mardeprata.app.model;

import jakarta.persistence.*;

@Entity
@Table(name = "restaurant_tables")
public class RestaurantTable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "table_number", unique = true, nullable = false)
    private Integer tableNumber;

    private Integer capacity = 4;
    private Boolean active = true;

    @Column(name = "qr_code_url")
    private String qrCodeUrl; // URL da imagem QR gerada

    // Getters e Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public Integer getTableNumber() { return tableNumber; }
    public void setTableNumber(Integer tableNumber) { this.tableNumber = tableNumber; }
    public Integer getCapacity() { return capacity; }
    public void setCapacity(Integer capacity) { this.capacity = capacity; }
    public Boolean getActive() { return active; }
    public void setActive(Boolean active) { this.active = active; }
    public String getQrCodeUrl() { return qrCodeUrl; }
    public void setQrCodeUrl(String qrCodeUrl) { this.qrCodeUrl = qrCodeUrl; }
}
