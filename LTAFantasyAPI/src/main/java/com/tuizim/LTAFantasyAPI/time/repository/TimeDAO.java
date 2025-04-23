package com.tuizim.LTAFantasyAPI.time.repository;

import com.tuizim.LTAFantasyAPI.time.model.Time;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TimeDAO extends JpaRepository<Time, Integer> {
}
