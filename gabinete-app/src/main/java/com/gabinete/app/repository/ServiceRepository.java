package com.gabinete.app.repository;

import com.gabinete.app.model.Service;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface ServiceRepository extends JpaRepository<Service, Long> {
    List<Service> findByActiveTrueOrderByDisplayOrderAsc();
}
