package com.mardeprata.app.repository;

import com.mardeprata.app.model.TableOrder;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface TableOrderRepository extends JpaRepository<TableOrder, Long> {
    List<TableOrder> findByStatusOrderByCreatedAtDesc(TableOrder.Status status);
    List<TableOrder> findByTableNumberOrderByCreatedAtDesc(Integer tableNumber);
    List<TableOrder> findAllByOrderByCreatedAtDesc();
    List<TableOrder> findByCreatedAtAfterOrderByCreatedAtDesc(java.time.LocalDateTime after);
}
