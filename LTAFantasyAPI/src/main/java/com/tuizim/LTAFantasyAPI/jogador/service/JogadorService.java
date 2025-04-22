package com.tuizim.LTAFantasyAPI.jogador.service;

import com.tuizim.LTAFantasyAPI.jogador.model.Jogador;
import com.tuizim.LTAFantasyAPI.jogador.model.Rota;
import com.tuizim.LTAFantasyAPI.jogador.repository.JogadorDAO;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

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
        List<Jogador> newJogadores = new ArrayList<>();
        for (Jogador jogador : jogadores) {
            jogador.setNickname(jogador.getNickname().toUpperCase());
            if (!jogadorDAO.existsByNickname(jogador.getNickname()) ){
                newJogadores.add(jogador);
            }
        }
        return jogadorDAO.saveAll(newJogadores);
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
        List<Jogador> JogadoresUPD = new ArrayList<>();
        for (Jogador jogador : jogadores) {
            Jogador exist_jogador = jogadorDAO.findByNickname(jogador.getNickname()).orElse(null);
            if (exist_jogador == null) {
                continue;
            }
            jogador.setNickname(jogador.getNickname().toUpperCase());
            jogador.setId(exist_jogador.getId());
            JogadoresUPD.add(jogador);
        }
        return jogadorDAO.saveAll(JogadoresUPD);
    }

    /* METODOS DELETE*/

    public void deleteJogador(long id) {
        if (!jogadorDAO.existsById(id)) {
            throw new IllegalArgumentException("Jogador nao encontrado");
        }
        jogadorDAO.deleteById(id);
    }
}
