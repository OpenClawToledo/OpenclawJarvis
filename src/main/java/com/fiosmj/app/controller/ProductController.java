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

        // 4. Produto Teste 🧪
        products.add(new Product(
            4L,
            "Produto Teste 🧪",
            "Produto de teste para validar o fluxo de pagamento. Valor simbólico de 1€ (R$6,10). Pode remover após os testes!",
            6.10,
            "/img/caneta.jpg",
            "Teste",
            null,
            99
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
