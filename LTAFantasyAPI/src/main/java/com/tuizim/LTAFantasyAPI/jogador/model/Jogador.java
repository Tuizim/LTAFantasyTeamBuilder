package com.tuizim.LTAFantasyAPI.jogador.model;

import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.tuizim.LTAFantasyAPI.util.PercentDoubleDeserializer;
import com.tuizim.LTAFantasyAPI.util.StringToDoubleDeserializer;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Table(name = "jogador")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Jogador {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;
    @Column(unique = true, nullable = false)
    private String nickname;
    @Enumerated(EnumType.STRING)
    private Rota rota;
    @Column
    private int jogos;
    @Column
    private double win_rate;
    @Column
    private double kda;
    @Column
    private double cs_minuto;
    @Column
    private double participa_abate;
    @Column
    private double media_ponto;
    @Column
    private double ultimo_ponto;
    @Column
    private double valor_atual;
    @Column
    @Enumerated(EnumType.STRING)
    private Liga liga;
}

