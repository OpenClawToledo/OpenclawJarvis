package com.gabinete.app.model;

import jakarta.persistence.*;

@Entity
@Table(name = "services")
public class Service {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String namePt;

    @Column(nullable = false)
    private String nameZh;

    @Column(columnDefinition = "TEXT")
    private String descriptionPt;

    @Column(columnDefinition = "TEXT")
    private String descriptionZh;

    private String icon; // nome do ícone (FontAwesome)
    private Boolean active = true;
    private Integer displayOrder = 0;

    // Getters e Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getNamePt() { return namePt; }
    public void setNamePt(String namePt) { this.namePt = namePt; }
    public String getNameZh() { return nameZh; }
    public void setNameZh(String nameZh) { this.nameZh = nameZh; }
    public String getDescriptionPt() { return descriptionPt; }
    public void setDescriptionPt(String descriptionPt) { this.descriptionPt = descriptionPt; }
    public String getDescriptionZh() { return descriptionZh; }
    public void setDescriptionZh(String descriptionZh) { this.descriptionZh = descriptionZh; }
    public String getIcon() { return icon; }
    public void setIcon(String icon) { this.icon = icon; }
    public Boolean getActive() { return active; }
    public void setActive(Boolean active) { this.active = active; }
    public Integer getDisplayOrder() { return displayOrder; }
    public void setDisplayOrder(Integer displayOrder) { this.displayOrder = displayOrder; }
}
