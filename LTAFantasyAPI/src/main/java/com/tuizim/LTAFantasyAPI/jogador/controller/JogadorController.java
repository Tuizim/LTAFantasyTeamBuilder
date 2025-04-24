package com.tuizim.LTAFantasyAPI.jogador.controller;

import com.tuizim.LTAFantasyAPI.jogador.model.Jogador;
import com.tuizim.LTAFantasyAPI.jogador.model.Liga;
import com.tuizim.LTAFantasyAPI.jogador.model.Rota;
import com.tuizim.LTAFantasyAPI.jogador.service.JogadorService;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RequestMapping("jogadores")
@RestController
@RequiredArgsConstructor
@Tag(name = "Jogadores", description = "CRUD e buscas individuais de jogadores")
public class JogadorController {
    private final JogadorService jogadorService;

    @GetMapping()
    public ResponseEntity<List<Jogador>> buscarJogadores(@RequestParam(required = false) Rota rota, @RequestParam(required = false) Liga liga) {
        List<Jogador> jogadores = jogadorService.buscarTodosJogadores(rota, liga);
        return ResponseEntity.ok(jogadores);
    }

    @GetMapping("/{nickname}")
    public ResponseEntity<Jogador> buscarJogadorPorId(@PathVariable String nickname){
        return ResponseEntity.ok(jogadorService.buscarJogador(nickname));
    }

    @PostMapping
    public ResponseEntity<Jogador> salvarJogador(@RequestBody Jogador jogador){
        return ResponseEntity.ok(jogadorService.criarJogador(jogador));
    }

    @PutMapping()
    public ResponseEntity<Jogador> atualizarJogador(@RequestBody Jogador jogador){
        return ResponseEntity.ok(jogadorService.atualizarJogador(jogador));
    }

    @DeleteMapping()
    public ResponseEntity<String> excluirJogador(@RequestParam String nickname){
        return ResponseEntity.ok(jogadorService.deletarJogador(nickname));
    }
}
