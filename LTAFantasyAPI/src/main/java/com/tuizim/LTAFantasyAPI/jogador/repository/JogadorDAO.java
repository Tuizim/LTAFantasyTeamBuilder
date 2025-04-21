package com.tuizim.LTAFantasyAPI.jogador.repository;

import com.tuizim.LTAFantasyAPI.jogador.model.Jogador;
import com.tuizim.LTAFantasyAPI.jogador.model.Rota;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

public interface JogadorDAO extends JpaRepository<Jogador, Long> {
    Optional<Jogador> findByNickname(String nickname);
    List<Jogador> findByRota(Rota rota);
}
