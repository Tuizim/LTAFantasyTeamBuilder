package com.tuizim.LTAFantasyAPI.confronto.model;

import com.tuizim.LTAFantasyAPI.time.model.Time;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDate;

@Entity
@Table(name = "confronto")
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Confronto {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;

    @ManyToOne
    @JoinColumn(name = "id_time1")
    private Time time1;

    @ManyToOne
    @JoinColumn(name = "id_time2")
    private Time time2;

    @Column
    private LocalDate data_confronto;

}
