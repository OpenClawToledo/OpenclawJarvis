package com.mardeprata.app.repository;

import com.mardeprata.app.model.RestaurantTable;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;
import java.util.Optional;

public interface RestaurantTableRepository extends JpaRepository<RestaurantTable, Long> {
    List<RestaurantTable> findByActiveTrueOrderByTableNumberAsc();
    Optional<RestaurantTable> findByTableNumber(Integer tableNumber);
}
