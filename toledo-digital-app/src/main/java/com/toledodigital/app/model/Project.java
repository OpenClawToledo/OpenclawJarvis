package com.toledodigital.app.model;

import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDateTime;

@Entity
@Table(name = "projects")
@Data
public class Project {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String cliente;
    private String nomeprojeto;
    private String descricao;
    private String pacote; // essencial, standard, premium
    private String status; // PLANEAMENTO, EM_CURSO, REVISAO, ENTREGUE, ARQUIVADO

    // Financeiro
    private Double valorContratado;
    private Double valorRecebido;
    private String formaPagamento; // numerario, transferencia, mb_way

    // Datas
    private LocalDateTime dataInicio;
    private LocalDateTime dataEntregaPrevista;
    private LocalDateTime dataEntregaReal;
    private LocalDateTime dataCriacao;

    // Técnico
    private String dominio;
    private String servidorIp;
    private String repositorioGit;
    private String notasTecnicas;

    // Contacto
    private String clienteTelefone;
    private String clienteEmail;

    @PrePersist
    public void prePersist() {
        dataCriacao = LocalDateTime.now();
        if (status == null) status = "PLANEAMENTO";
    }
}
