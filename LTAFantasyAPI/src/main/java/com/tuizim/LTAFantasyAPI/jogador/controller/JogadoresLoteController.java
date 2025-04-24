package com.tuizim.LTAFantasyAPI.jogador.controller;

import com.tuizim.LTAFantasyAPI.jogador.model.Jogador;
import com.tuizim.LTAFantasyAPI.jogador.service.JogadorService;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RequestMapping("jogadores/lote")
@RestController
@RequiredArgsConstructor
@Tag(name = "Jogadores em Lote", description = "Operações de criação e atualização em massa")
public class JogadoresLoteController {
    private final JogadorService jogadorService;

    @PostMapping()
    public ResponseEntity<List<Jogador>> salvarJogadoresLote(@RequestBody List<Jogador> jogadores){
        return ResponseEntity.ok(jogadorService.criarJogadorLote(jogadores));
    }

    @PutMapping()
    public ResponseEntity<List<Jogador>> atualizarJogadoresLote(@RequestBody List<Jogador> jogadores){
        return ResponseEntity.ok(jogadorService.atualizarJogadorLote(jogadores));
    }
}
