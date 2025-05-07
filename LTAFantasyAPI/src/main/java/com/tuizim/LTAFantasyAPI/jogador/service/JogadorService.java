package com.tuizim.LTAFantasyAPI.jogador.service;

import com.tuizim.LTAFantasyAPI.config.ErrorMessages;
import com.tuizim.LTAFantasyAPI.config.SuccessMessages;
import com.tuizim.LTAFantasyAPI.jogador.model.Jogador;
import com.tuizim.LTAFantasyAPI.jogador.model.Liga;
import com.tuizim.LTAFantasyAPI.jogador.model.Rota;
import com.tuizim.LTAFantasyAPI.jogador.repository.JogadorDAO;
import com.tuizim.LTAFantasyAPI.time.model.Time;
import com.tuizim.LTAFantasyAPI.time.repository.TimeDAO;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
@RequiredArgsConstructor
public class JogadorService {

    private final JogadorDAO jogadorDAO;
    private final TimeDAO timeDAO;

    public List<Jogador> buscarTodosJogadores(Rota rota, Liga liga) {
        if (liga == null && rota == null) {
            return jogadorDAO.findAll();
        }
        else if (liga == null) {
            return jogadorDAO.findByRota(rota);
        }
        else if (rota == null) {
            return jogadorDAO.findByLiga(liga);
        }
        else{
            return jogadorDAO.findByRotaAndLiga(rota,liga);
        }
    }

    public Jogador buscarJogador(String nickname) {
        if (nickname !=null && !nickname.isBlank()) {
            return jogadorDAO.findByNickname(nickname.toUpperCase()).orElseThrow(()->new RuntimeException(String.format(ErrorMessages.JOGADOR_NOTFOUND_NICKNAME,nickname)));
        }
        else throw new RuntimeException(ErrorMessages.JOGADOR_INVALID_PARAMS);
    }

    public Jogador criarJogador(Jogador jogador) {
        jogador.setNickname(jogador.getNickname().toUpperCase());
        jogador.setId(0);
        if (jogadorDAO.existsByNickname(jogador.getNickname())) {
            throw new RuntimeException(ErrorMessages.JOGADOR_JUST_EXISTS);
        }
        if (jogador.getTime()!=null) {
            jogador.setTime(validarTimeJogador(jogador.getTime()));
        }
        return jogadorDAO.save(jogador);
    }

    public List<Jogador> criarJogadorLote(List<Jogador> jogadores) {
        List<Jogador> jogadoresLote = new ArrayList<>();
        for (Jogador jogador : jogadores) {
            jogador.setNickname(jogador.getNickname().toUpperCase());
            jogador.setId(0);
            if (jogador.getTime()!=null) {
                jogador.setTime(validarTimeJogador(jogador.getTime()));
            }
            if (!jogadorDAO.existsByNickname(jogador.getNickname())) {
                jogadoresLote.add(jogador);
            }
        }
        return jogadorDAO.saveAll(jogadoresLote);
    }

    public Jogador atualizarJogador(Jogador jogador) {
        jogador.setNickname(jogador.getNickname().toUpperCase());
        Jogador jogadorToUpdate = jogadorDAO.findByNickname(jogador.getNickname()).orElseThrow(()-> new RuntimeException(String.format(ErrorMessages.JOGADOR_NOTFOUND_NICKNAME,jogador.getNickname())));
        jogador.setId(jogadorToUpdate.getId());
        if (jogador.getTime()!=null) {
            jogador.setTime(validarTimeJogador(jogador.getTime()));
        }
        return jogadorDAO.save(jogador);
    }

    public List<Jogador> atualizarJogadorLote(List<Jogador> jogadores) {
        List<Jogador> jogadoresLote = new ArrayList<>();
        for (Jogador jogador : jogadores) {
            jogador.setNickname(jogador.getNickname().toUpperCase());
            Jogador jogadorToUpdate = jogadorDAO.findByNickname(jogador.getNickname()).orElse(null);
            if (jogador.getTime()!=null) {
                jogador.setTime(validarTimeJogador(jogador.getTime()));
            }
            if (jogadorToUpdate != null) {
                jogador.setId(jogadorToUpdate.getId());
                jogadoresLote.add(jogador);
            }
        }
        return jogadorDAO.saveAll(jogadoresLote);
    }

    public String deletarJogador(String nickname) {
        String nicknameFormated = nickname.toUpperCase();
        if (!jogadorDAO.existsByNickname(nicknameFormated)) {
            throw new RuntimeException(String.format(ErrorMessages.JOGADOR_NOTFOUND_NICKNAME,nicknameFormated));
        }
        Jogador jogador = jogadorDAO.findByNickname(nicknameFormated).orElseThrow(()->new RuntimeException(String.format(ErrorMessages.JOGADOR_NOTFOUND_NICKNAME,nicknameFormated)));
        jogadorDAO.delete(jogador);
        return SuccessMessages.JOGADOR_SUCCESS_DELETE;
    }

    public Time validarTimeJogador(Time time) {
        return timeDAO.findByNome(time.getNome()).orElse(null);
    }
}
