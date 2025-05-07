package com.tuizim.LTAFantasyAPI.confronto.service;

import com.tuizim.LTAFantasyAPI.config.ErrorMessages;
import com.tuizim.LTAFantasyAPI.config.SuccessMessages;
import com.tuizim.LTAFantasyAPI.confronto.model.Confronto;
import com.tuizim.LTAFantasyAPI.confronto.repository.ConfrontoDAO;
import com.tuizim.LTAFantasyAPI.time.model.Time;
import com.tuizim.LTAFantasyAPI.time.repository.TimeDAO;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
@RequiredArgsConstructor
public class ConfrontoService {
    private final ConfrontoDAO confrontoDAO;
    private final TimeDAO timeDAO;

    public Confronto tratarConfronto(Confronto confronto){
        confronto.getTime1().setNome(confronto.getTime1().getNome().toUpperCase());
        confronto.getTime2().setNome(confronto.getTime2().getNome().toUpperCase());

        String nomeTime1 = confronto.getTime1().getNome();
        String nomeTime2 = confronto.getTime2().getNome();
        if (nomeTime1.equals(nomeTime2)) {
            throw new RuntimeException(ErrorMessages.CONFRONTO_IT_SELF_ERROR);
        }

        Time time1 = timeDAO.findByNome(nomeTime1).orElseThrow(()->new RuntimeException(String.format(ErrorMessages.TIME_NOTFOUND_NOME, nomeTime1)));
        Time time2 = timeDAO.findByNome(nomeTime2).orElseThrow(()->new RuntimeException(String.format(ErrorMessages.TIME_NOTFOUND_NOME, nomeTime2)));

        confronto.setId(0);
        confronto.setTime1(time1);
        confronto.setTime2(time2);
        return confronto;
    }

    public Confronto criarConfronto(Confronto confronto) {
        Confronto confrontoTratado = tratarConfronto(confronto);
        if (confrontoDAO.existsByTimesEitherOrderAndData(confrontoTratado.getId(),confrontoTratado.getId(),confrontoTratado.getData_confronto())){
            throw new RuntimeException(ErrorMessages.CONFRONTO_JUST_EXISTS);
        }
        return confrontoDAO.save(confrontoTratado);
    }
    public List<Confronto> criarConfrontoLote(List<Confronto> confrontos) {
        List<Confronto> newConfrontos = new ArrayList<>();
        for (Confronto confronto : confrontos) {
            Confronto confrontoTratado = tratarConfronto(confronto);
            if (!confrontoDAO.existsByTimesEitherOrderAndData(confrontoTratado.getId(),confrontoTratado.getId(),confrontoTratado.getData_confronto())){
                newConfrontos.add(confrontoTratado);
            }
        }
        return confrontoDAO.saveAll(newConfrontos);
    }

    public String apagarConfronto(Confronto confronto) {
        Confronto confrontoTratado = tratarConfronto(confronto);
        Long id = confrontoDAO.findIdByTimesEitherOrderAndData(
                confrontoTratado.getTime1().getId(),
                confrontoTratado.getTime2().getId(),
                confrontoTratado.getData_confronto()).orElseThrow(()->new RuntimeException(ErrorMessages.CONFRONTO_NOT_EXISTS));
        confrontoDAO.deleteById(id);
        return SuccessMessages.SUCCESS;
    }

    public List<Confronto> buscarConfrontos(){
        return confrontoDAO.findAll();
    }

}
