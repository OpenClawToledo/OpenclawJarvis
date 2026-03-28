package com.toledodigital.app.model;

import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDateTime;

@Entity
@Table(name = "leads")
@Data
public class Lead {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    // Identificação
    private String nome;
    private String empresa;
    private String setor; // restaurante, gabinete, clinica, comercio, etc
    private String telefone;
    private String email;
    private String cidade;
    private String pais; // PT, BR

    // Pipeline
    private String status; // NOVO, CONTACTADO, PROPOSTA, NEGOCIACAO, FECHADO, PERDIDO
    private String canal; // whatsapp, email, instagram, google_maps, referencia, cold_call
    private String origem; // quem indicou ou como foi encontrado

    // Projeto
    private String pacoteInteresse; // essencial, standard, premium, custom
    private Double valorEstimado;
    private String notasVenda;

    // Datas
    private LocalDateTime dataCriacao;
    private LocalDateTime dataUltimoContacto;
    private LocalDateTime dataProximoFollowUp;
    private LocalDateTime dataFecho;

    @PrePersist
    public void prePersist() {
        dataCriacao = LocalDateTime.now();
        if (status == null) status = "NOVO";
    }
}
