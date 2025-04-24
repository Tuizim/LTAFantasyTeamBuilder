package com.tuizim.LTAFantasyAPI.time.repository;

import com.tuizim.LTAFantasyAPI.time.model.Time;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface TimeDAO extends JpaRepository<Time, Integer> {
    Optional<Time> findByNome(String Nome);
    boolean existsByNome(String Nome);
}
