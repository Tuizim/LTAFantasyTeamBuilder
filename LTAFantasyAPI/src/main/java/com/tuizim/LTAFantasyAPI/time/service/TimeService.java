package com.tuizim.LTAFantasyAPI.time.service;

import com.tuizim.LTAFantasyAPI.config.ErrorMessages;
import com.tuizim.LTAFantasyAPI.config.SuccessMessages;
import com.tuizim.LTAFantasyAPI.time.model.Time;
import com.tuizim.LTAFantasyAPI.time.repository.TimeDAO;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
@RequiredArgsConstructor
public class TimeService {
    private final TimeDAO timeDAO;

    public Time criarTime(Time time) {
        if (timeDAO.existsByNome(time.getNome())) {
            throw new RuntimeException(ErrorMessages.TIME_JUST_EXISTS);
        }
        time.setId(0);
        time.setNome(time.getNome().toUpperCase());
        return timeDAO.save(time);
    }

    public List<Time> criarTimeLote(List<Time> times) {
        List<Time> timesLote = new ArrayList<>();
        for (Time time : times) {
            if (!timeDAO.existsByNome(time.getNome())) {
                time.setId(0);
                time.setNome(time.getNome().toUpperCase());
                timesLote.add(time);
            }
        }
        return timeDAO.saveAll(timesLote);
    }

    public List<Time> buscarTimes() {
        return timeDAO.findAll();
    }

    public Time buscarTimePorNome(String nome) {
        return timeDAO.findByNome(nome.toUpperCase())
                .orElseThrow(() -> new RuntimeException(String.format(ErrorMessages.TIME_NOTFOUND_NOME, nome.toUpperCase())));
    }

    public Time atualizarTime(Time time) {
        time.setNome(time.getNome().toUpperCase());
        Time timeSalvo = timeDAO.findByNome(time.getNome()).orElse(null);
        if (timeSalvo == null) {
            throw new RuntimeException(String.format(ErrorMessages.TIME_NOTFOUND_NOME, time.getNome().toUpperCase()));
        }
        timeSalvo.setId(time.getId());
        return timeDAO.save(timeSalvo);
    }

    public List<Time> atualizarTimeLote(List<Time> times) {
        List<Time> timeLote = new ArrayList<>();
        for (Time time : times) {
            time.setNome(time.getNome().toUpperCase());
            Time timeSalvo = timeDAO.findByNome(time.getNome()).orElse(null);
            if (timeSalvo != null) {
                time.setId(timeSalvo.getId());
                timeLote.add(timeSalvo);
            }
        }
        return timeDAO.saveAll(timeLote);
    }

    public String deletarTime(String nome) {
        String nomeFormatado = nome.toUpperCase();
        if (!timeDAO.existsByNome(nomeFormatado)) {
            throw new RuntimeException(String.format(ErrorMessages.TIME_NOTFOUND_NOME, nomeFormatado));
        }
        Time time = timeDAO.findByNome(nomeFormatado).orElseThrow(() -> new RuntimeException(String.format(ErrorMessages.TIME_NOTFOUND_NOME, nomeFormatado)));
        timeDAO.delete(time);
        return SuccessMessages.TIME_SUCCESS_DELETE;
    }
}
