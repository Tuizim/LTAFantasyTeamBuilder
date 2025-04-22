package com.tuizim.LTAFantasyAPI.jogador.service;

import com.tuizim.LTAFantasyAPI.jogador.model.Jogador;
import com.tuizim.LTAFantasyAPI.jogador.model.Rota;
import com.tuizim.LTAFantasyAPI.jogador.repository.JogadorDAO;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;

@Service
@RequiredArgsConstructor
public class JogadorService {

    private final JogadorDAO jogadorDAO;

    /* METODOS BUSCA*/

    public List<Jogador> getAllJogadores(Sort sort) {
        return jogadorDAO.findAll(sort);
    }
    public Jogador getJogadorById(long id) {
        return jogadorDAO.getReferenceById(id);
    }
    public Jogador getJogadorByNickname(String nickname) {
        return jogadorDAO.findByNickname(nickname).orElseThrow(()->new RuntimeException("Jogador nao encontrado"));
    }
    public List<Jogador> getJogadorByRota(Rota rota) {
        return jogadorDAO.findByRota(rota);
    }

    /* METODOS ADD*/

    public Jogador createJogador(Jogador jogador) {
        jogador.setNickname(jogador.getNickname().toUpperCase());
        return jogadorDAO.save(jogador);
    }
    public List<Jogador> createJogadores(List<Jogador> jogadores) {
        for (Jogador jogador : jogadores) {
            jogador.setNickname(jogador.getNickname().toUpperCase());
        }
        return jogadorDAO.saveAll(jogadores);
    }

    /* METODOS ATUALIZAR*/

    public Jogador updateJogador(Jogador jogador) {
        if (jogador.getId() <= 0) {
            throw new IllegalArgumentException("ID inválido para atualização.");
        }
        return jogadorDAO.save(jogador);
    }
    public List<Jogador> updateJogadores(List<Jogador> jogadores) {
        return jogadorDAO.saveAll(jogadores);
    }
    public List<Jogador> updateJogadoresInLoteByNickname(List<Jogador> jogadores) {
        List<Jogador> newJogadores = new ArrayList<>();
        for (Jogador jogador : jogadores) {
            jogador.setNickname(jogador.getNickname().toUpperCase());
            Jogador updatedjogador = jogadorDAO.findByNickname(jogador.getNickname()).orElse(null);
            if (updatedjogador == null) {
                continue;
            }
            updatedjogador.setRota(jogador.getRota());
            updatedjogador.setJogos(jogador.getJogos());
            updatedjogador.setWin_rate(jogador.getWin_rate());
            updatedjogador.setKda(jogador.getKda());
            updatedjogador.setCs_minuto(jogador.getCs_minuto());
            updatedjogador.setParticipa_abate(jogador.getParticipa_abate());
            updatedjogador.setMedia_ponto(jogador.getMedia_ponto());
            updatedjogador.setUltimo_ponto(jogador.getUltimo_ponto());
            updatedjogador.setValor_atual(jogador.getValor_atual());
            newJogadores.add(updatedjogador);
        }
        return jogadorDAO.saveAll(newJogadores);
    }
    /* METODOS DELETE*/
    public void deleteJogador(long id) {
        if (!jogadorDAO.existsById(id)) {
            throw new IllegalArgumentException("Jogador nao encontrado");
        }
        jogadorDAO.deleteById(id);
    }
}
