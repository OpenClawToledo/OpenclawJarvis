package com.mardeprata.app.model;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "menu_items")
public class MenuItem {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String name;

    private String description;

    @Column(nullable = false)
    private Double price;

    private String imageUrl;

    @Column(nullable = false)
    private String category; // Entradas, Pratos, Sopas, Sobremesas, Bebidas

    // Alergénios (obrigatório por lei em Portugal)
    private Boolean hasGluten = false;
    private Boolean hasCrustaceans = false;
    private Boolean hasEggs = false;
    private Boolean hasFish = false;
    private Boolean hasPeanuts = false;
    private Boolean hasSoy = false;
    private Boolean hasMilk = false;
    private Boolean hasNuts = false;
    private Boolean hasCelery = false;
    private Boolean hasMustard = false;
    private Boolean hasSeeds = false;
    private Boolean hasSulphites = false;
    private Boolean hasLupin = false;
    private Boolean hasMolluscs = false;

    private Boolean active = true;
    private Boolean featured = false;
    private Integer displayOrder = 0;

    private Boolean spicy = false;
    private Boolean vegetarian = false;
    private Boolean vegan = false;

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
    public Boolean getHasGluten() { return hasGluten; }
    public void setHasGluten(Boolean hasGluten) { this.hasGluten = hasGluten; }
    public Boolean getHasCrustaceans() { return hasCrustaceans; }
    public void setHasCrustaceans(Boolean hasCrustaceans) { this.hasCrustaceans = hasCrustaceans; }
    public Boolean getHasEggs() { return hasEggs; }
    public void setHasEggs(Boolean hasEggs) { this.hasEggs = hasEggs; }
    public Boolean getHasFish() { return hasFish; }
    public void setHasFish(Boolean hasFish) { this.hasFish = hasFish; }
    public Boolean getHasPeanuts() { return hasPeanuts; }
    public void setHasPeanuts(Boolean hasPeanuts) { this.hasPeanuts = hasPeanuts; }
    public Boolean getHasSoy() { return hasSoy; }
    public void setHasSoy(Boolean hasSoy) { this.hasSoy = hasSoy; }
    public Boolean getHasMilk() { return hasMilk; }
    public void setHasMilk(Boolean hasMilk) { this.hasMilk = hasMilk; }
    public Boolean getHasNuts() { return hasNuts; }
    public void setHasNuts(Boolean hasNuts) { this.hasNuts = hasNuts; }
    public Boolean getHasCelery() { return hasCelery; }
    public void setHasCelery(Boolean hasCelery) { this.hasCelery = hasCelery; }
    public Boolean getHasMustard() { return hasMustard; }
    public void setHasMustard(Boolean hasMustard) { this.hasMustard = hasMustard; }
    public Boolean getHasSeeds() { return hasSeeds; }
    public void setHasSeeds(Boolean hasSeeds) { this.hasSeeds = hasSeeds; }
    public Boolean getHasSulphites() { return hasSulphites; }
    public void setHasSulphites(Boolean hasSulphites) { this.hasSulphites = hasSulphites; }
    public Boolean getHasLupin() { return hasLupin; }
    public void setHasLupin(Boolean hasLupin) { this.hasLupin = hasLupin; }
    public Boolean getHasMolluscs() { return hasMolluscs; }
    public void setHasMolluscs(Boolean hasMolluscs) { this.hasMolluscs = hasMolluscs; }
    public Boolean getActive() { return active; }
    public void setActive(Boolean active) { this.active = active; }
    public Boolean getFeatured() { return featured; }
    public void setFeatured(Boolean featured) { this.featured = featured; }
    public Integer getDisplayOrder() { return displayOrder; }
    public void setDisplayOrder(Integer displayOrder) { this.displayOrder = displayOrder; }
    public Boolean getSpicy() { return spicy; }
    public void setSpicy(Boolean spicy) { this.spicy = spicy; }
    public Boolean getVegetarian() { return vegetarian; }
    public void setVegetarian(Boolean vegetarian) { this.vegetarian = vegetarian; }
    public Boolean getVegan() { return vegan; }
    public void setVegan(Boolean vegan) { this.vegan = vegan; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public LocalDateTime getUpdatedAt() { return updatedAt; }
}
