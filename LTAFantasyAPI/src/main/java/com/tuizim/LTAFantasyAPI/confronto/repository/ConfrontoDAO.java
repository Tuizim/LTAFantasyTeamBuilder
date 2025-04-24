package com.tuizim.LTAFantasyAPI.confronto.repository;

import com.tuizim.LTAFantasyAPI.confronto.model.Confronto;
import com.tuizim.LTAFantasyAPI.time.model.Time;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.time.LocalDate;
import java.util.Optional;

public interface ConfrontoDAO extends JpaRepository<Confronto, Long> {
    @Query("""
        SELECT CASE WHEN COUNT(c)>0 THEN true ELSE false END
        FROM Confronto c
        WHERE (
            (c.time1.id = :t1 AND c.time2.id = :t2)
         OR (c.time1.id = :t2 AND c.time2.id = :t1)
        )
        AND c.data_confronto = :data
    """)
    boolean existsByTimesEitherOrderAndData(
            @Param("t1") Long time1Id,
            @Param("t2") Long time2Id,
            @Param("data") LocalDate data
    );
    @Query("""
        SELECT c.id
        FROM Confronto c
        WHERE (
            (c.time1.id = :t1 AND c.time2.id = :t2)
         OR (c.time1.id = :t2 AND c.time2.id = :t1)
        )
        AND c.data_confronto = :data
    """)
    Optional<Long> findIdByTimesEitherOrderAndData(
            @Param("t1") Long time1Id,
            @Param("t2") Long time2Id,
            @Param("data") LocalDate data
    );
}
