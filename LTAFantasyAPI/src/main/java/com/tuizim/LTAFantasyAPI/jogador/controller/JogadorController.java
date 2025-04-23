package com.tuizim.LTAFantasyAPI.jogador.controller;

import com.tuizim.LTAFantasyAPI.jogador.model.Jogador;
import com.tuizim.LTAFantasyAPI.jogador.model.Liga;
import com.tuizim.LTAFantasyAPI.jogador.model.Rota;
import com.tuizim.LTAFantasyAPI.jogador.service.JogadorService;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Sort;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RequestMapping("jogadores")
@RestController
@RequiredArgsConstructor
public class JogadorController {
    private final JogadorService jogadorService;

    @GetMapping()
    public ResponseEntity<List<Jogador>> buscarJogadores(
            @RequestParam(required = false) Rota rota,
            @RequestParam(required = false) Liga liga,
            @RequestParam(defaultValue = "nickname") String sortBy,
            @RequestParam(defaultValue = "asc") String ordem )
    {
        Sort sort = ordem.equalsIgnoreCase("desc")? Sort.by(sortBy).descending() : Sort.by(sortBy).ascending();
        List<Jogador> jogadores = jogadorService.buscarTodosJogadores(sort, rota, liga);
        return ResponseEntity.ok(jogadores);
    }
    @GetMapping("id/{id}")
    public ResponseEntity<Jogador> buscarJogadorPorId(@PathVariable long id){
        return ResponseEntity.ok(jogadorService.buscarJogador(id,null));
    }
    @GetMapping("nick/{nickname}")
    public ResponseEntity<Jogador> buscarJogadorPorId(@PathVariable String nickname){
        return ResponseEntity.ok(jogadorService.buscarJogador(0,nickname));
    }
}
