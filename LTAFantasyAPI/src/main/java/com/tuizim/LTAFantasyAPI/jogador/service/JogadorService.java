package com.tuizim.LTAFantasyAPI.jogador.service;

import com.tuizim.LTAFantasyAPI.config.ErrorMessages;
import com.tuizim.LTAFantasyAPI.jogador.model.Jogador;
import com.tuizim.LTAFantasyAPI.jogador.model.Liga;
import com.tuizim.LTAFantasyAPI.jogador.model.Rota;
import com.tuizim.LTAFantasyAPI.jogador.repository.JogadorDAO;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class JogadorService {

    private final JogadorDAO jogadorDAO;

    public List<Jogador> buscarTodosJogadores(Sort sort, Rota rota, Liga liga) {
        if (liga == null && rota == null) {
            return jogadorDAO.findAll(sort);
        }
        else if (liga == null && rota != null) {
            return jogadorDAO.findByRota(rota);
        }
        else if (liga != null && rota == null) {
            return jogadorDAO.findByLiga(liga);
        }
        else{
            return jogadorDAO.findByRotaAndLiga(rota,liga);
        }
    }

    public Jogador buscarJogador(long id, String nickname) {
        if (id>0){
            return jogadorDAO.findById(id).orElseThrow(()->new RuntimeException(String.format(ErrorMessages.JOGADOR_NOTFOUND_ID,id)));
        }
        else if (nickname !=null && !nickname.isBlank()) {
            return jogadorDAO.findByNickname(nickname.toUpperCase()).orElseThrow(()->new RuntimeException(String.format(ErrorMessages.JOGADOR_NOTFOUND_NICKNAME,nickname)));
        }
        else throw new RuntimeException(ErrorMessages.JOGADOR_INVALID_PARAMS);
    }

}
