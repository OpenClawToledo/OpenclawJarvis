package com.mardeprata.app.controller;

import com.mardeprata.app.model.MenuItem;
import com.mardeprata.app.repository.MenuItemRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/api/menu")
public class MenuController {

    @Autowired
    private MenuItemRepository menuItemRepository;

    // GET /api/menu — todos os items activos agrupados por categoria
    @GetMapping
    public ResponseEntity<Map<String, List<MenuItem>>> getMenu() {
        List<MenuItem> items = menuItemRepository.findByActiveTrueOrderByDisplayOrderAsc();
        Map<String, List<MenuItem>> grouped = items.stream()
                .collect(Collectors.groupingBy(MenuItem::getCategory));
        return ResponseEntity.ok(grouped);
    }

    // GET /api/menu/list — lista flat de todos os items activos
    @GetMapping("/list")
    public ResponseEntity<List<MenuItem>> getMenuList() {
        return ResponseEntity.ok(menuItemRepository.findByActiveTrueOrderByDisplayOrderAsc());
    }

    // GET /api/menu/featured — items em destaque
    @GetMapping("/featured")
    public ResponseEntity<List<MenuItem>> getFeatured() {
        return ResponseEntity.ok(menuItemRepository.findByFeaturedTrueAndActiveTrue());
    }

    // GET /api/menu/category/{category}
    @GetMapping("/category/{category}")
    public ResponseEntity<List<MenuItem>> getByCategory(@PathVariable String category) {
        return ResponseEntity.ok(
            menuItemRepository.findByCategoryAndActiveTrueOrderByDisplayOrderAsc(category)
        );
    }

    // GET /api/menu/{id}
    @GetMapping("/{id}")
    public ResponseEntity<MenuItem> getItem(@PathVariable Long id) {
        return menuItemRepository.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }
}
