package com.mardeprata.app.repository;

import com.mardeprata.app.model.MenuItem;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface MenuItemRepository extends JpaRepository<MenuItem, Long> {
    List<MenuItem> findByActiveTrueOrderByDisplayOrderAsc();
    List<MenuItem> findByCategoryAndActiveTrueOrderByDisplayOrderAsc(String category);
    List<MenuItem> findByFeaturedTrueAndActiveTrue();
}
