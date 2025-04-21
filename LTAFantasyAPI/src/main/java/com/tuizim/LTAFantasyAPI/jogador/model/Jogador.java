package com.tuizim.LTAFantasyAPI.jogador.model;

import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.tuizim.LTAFantasyAPI.util.PercentDoubleDeserializer;
import com.tuizim.LTAFantasyAPI.util.StringToDoubleDeserializer;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity(name = "jogador")
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
    @JsonDeserialize(using = PercentDoubleDeserializer.class)
    private double win_rate;
    @Column
    @JsonDeserialize(using = StringToDoubleDeserializer.class)
    private double kda;
    @Column
    @JsonDeserialize(using = StringToDoubleDeserializer.class)
    private double cs_minuto;
    @Column
    @JsonDeserialize(using = PercentDoubleDeserializer.class)
    private double participa_abate;
    @Column
    @JsonDeserialize(using = StringToDoubleDeserializer.class)
    private double media_ponto;
    @Column
    @JsonDeserialize(using = StringToDoubleDeserializer.class)
    private double ultimo_ponto;
    @Column
    @JsonDeserialize(using = StringToDoubleDeserializer.class)
    private double valor_atual;
    @Column
    @JsonDeserialize(using = StringToDoubleDeserializer.class)
    private double flutuacao_mercado;
}

