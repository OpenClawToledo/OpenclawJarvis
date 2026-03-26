package com.fiosmj.app.controller;

import com.fiosmj.app.model.Product;
import org.springframework.web.bind.annotation.*;

import java.util.*;

@RestController
@RequestMapping("/api")
public class ProductController {

    private final List<Product> products;

    public ProductController() {
        products = new ArrayList<>();

        // 1. Cropped Halter Brasil 🇧🇷
        products.add(new Product(
            1L,
            "Cropped Halter Brasil 🇧🇷",
            "Cropped de crochê com tema Copa do Mundo 2026! Feito à mão com fio 100% algodão nas cores da bandeira do Brasil. Perfeito para torcer com muito estilo! 🎉",
            100.0,
            "/img/cropped-brasil.jpg",
            "Roupas",
            List.of(
                Map.of("size", "P", "price", 100.0),
                Map.of("size", "M", "price", 120.0),
                Map.of("size", "G", "price", 150.0)
            ),
            5
        ));

        // 2. Amigurumi Nossa Senhora 🙏
        products.add(new Product(
            2L,
            "Amigurumi Nossa Senhora 🙏",
            "Amigurumi artesanal da Nossa Senhora Aparecida, feito com muito carinho e devoção. Detalhes em dourado, acabamento delicado. Uma peça especial para presentear ou ter em casa. ✨",
            80.0,
            "/img/nossa-senhora.jpg",
            "Amigurumi",
            null,
            3
        ));

        // 3. Caneta Decorada ✏️
        products.add(new Product(
            3L,
            "Caneta Decorada ✏️",
            "Caneta decorada com crochê artesanal colorido. Ótima opção de presente criativo e único! Disponível em diversas cores. 🌈",
            20.0,
            "/img/caneta.jpg",
            "Acessórios",
            null,
            10
        ));



        // 5. Bolsa de Anéis Rose 🌸
        products.add(new Product(
            5L,
            "Bolsa de Anéis Rose 🌸",
            "Bolsa artesanal de crochê em técnica de anéis, feita com fio de polipropileno na cor rose/terracota. Forro interno de cetim rose metálico e alça hexagonal em resina âmbar. Peça única, feita à mão com muito carinho. Preço a partir de R$250 — varia conforme tamanho e modelo. Sob encomenda.",
            250.0,
            "/uploads/bolsas/bolsa-aneis-rose.jpg",
            "Bolsas",
            null,
            1
        ));

        // 6. Amigurumi Cachorrinho 🐶
        products.add(new Product(
            6L,
            "Amigurumi Cachorrinho 🐶",
            "Amigurumi cachorrinho feito à mão com fio de algodão, acabamento delicado, olhinhos bordados e coleirinha vermelha. Uma peça única e cheia de personalidade! Preço a partir de R$120 — varia conforme tamanho e modelo. Sob encomenda.",
            120.0,
            "/uploads/amigurumi/amigurumi-cachorro-bege.jpg",
            "Amigurumi",
            null,
            1
        ));

        // 8. Bolsa Cordão Rayontex Bege 🧵
        products.add(new Product(
            8L,
            "Bolsa Cordão Bege 🧵",
            "Bolsa artesanal feita com cordão Rayontex Bege 1200TEX 100% polipropileno — material resistente e de acabamento premium. Peça estruturada, feita à mão com muito cuidado. Preço a partir de R$250 — varia conforme tamanho e modelo. Sob encomenda.",
            250.0,
            "/uploads/bolsas/cordao-rayontex-bege.jpg",
            "Bolsas",
            null,
            1
        ));

        // 7. Amigurumi Boneca 🎀
        products.add(new Product(
            7L,
            "Amigurumi Boneca 🎀",
            "Boneca amigurumi artesanal com cabelo cacheado e vestidinho colorido feito à mão. Disponível em diversas cores e modelos. Peça perfeita para presentear! Preço a partir de R$120 — varia conforme tamanho e modelo. Sob encomenda.",
            120.0,
            "/uploads/amigurumi/amigurumi-bonecas.jpg",
            "Amigurumi",
            null,
            1
        ));

        // 9. Cropped de Crochê 🧶
        products.add(new Product(
            9L,
            "Cropped de Crochê 🧶",
            "Cropped artesanal feito à mão com fio de qualidade. Peça única, cheia de estilo e personalidade! Disponível nos tamanhos P, M e G.",
            100.0,
            "/uploads/roupas/cropped-novo.jpg",
            "Roupas",
            List.of(
                Map.of("size", "P", "price", 100.0),
                Map.of("size", "M", "price", 120.0),
                Map.of("size", "G", "price", 140.0)
            ),
            3
        ));
    }

    @GetMapping("/products")
    public List<Product> getAllProducts() {
        return products;
    }

    @GetMapping("/products/{id}")
    public Product getProductById(@PathVariable Long id) {
        return products.stream()
            .filter(p -> p.getId().equals(id))
            .findFirst()
            .orElseThrow(() -> new RuntimeException("Produto não encontrado: " + id));
    }

    @GetMapping("/health")
    public Map<String, String> health() {
        return Map.of("status", "ok", "app", "Fios MJ API");
    }
}
