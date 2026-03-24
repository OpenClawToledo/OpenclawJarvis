package com.fiosmj.app.model;

import java.util.List;
import java.util.Map;

public class Product {
    private Long id;
    private String name;
    private String description;
    private Double price;
    private String imageUrl;
    private String category;
    private List<Map<String, Object>> sizes; // [{size: "P", price: 100.0}, ...]
    private Integer stock;

    public Product() {}

    public Product(Long id, String name, String description, Double price,
                   String imageUrl, String category, List<Map<String, Object>> sizes) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.price = price;
        this.imageUrl = imageUrl;
        this.category = category;
        this.sizes = sizes;
    }

    public Product(Long id, String name, String description, Double price,
                   String imageUrl, String category, List<Map<String, Object>> sizes, Integer stock) {
        this(id, name, description, price, imageUrl, category, sizes);
        this.stock = stock;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    public Double getPrice() { return price; }
    public void setPrice(Double price) { this.price = price; }

    public String getImageUrl() { return imageUrl; }
    public void setImageUrl(String imageUrl) { this.imageUrl = imageUrl; }

    public String getCategory() { return category; }
    public void setCategory(String category) { this.category = category; }

    public List<Map<String, Object>> getSizes() { return sizes; }
    public void setSizes(List<Map<String, Object>> sizes) { this.sizes = sizes; }

    public Integer getStock() { return stock; }
    public void setStock(Integer stock) { this.stock = stock; }
}
