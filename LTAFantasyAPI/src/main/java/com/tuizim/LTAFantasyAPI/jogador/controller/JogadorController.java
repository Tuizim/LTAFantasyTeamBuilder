package com.tuizim.LTAFantasyAPI.jogador.controller;

import com.tuizim.LTAFantasyAPI.jogador.model.Jogador;
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
    public ResponseEntity<List<Jogador>> listarT(
            @RequestParam(defaultValue = "nickname") String sortBy,
            @RequestParam(defaultValue = "asc") String ordem )
    {
        Sort sort = ordem.equalsIgnoreCase("disc")? Sort.by(sortBy).descending() : Sort.by(sortBy).ascending();
        List<Jogador> jogadores = jogadorService.getAllJogadores(sort);
        return ResponseEntity.ok(jogadores);
    }
    @GetMapping("/{id}")
    public ResponseEntity<Jogador> getJogador(@RequestParam Long id){
        return ResponseEntity.ok(jogadorService.getJogadorById(id));
    }
    @GetMapping("/rota/{rota}")
    public ResponseEntity<List<Jogador>> getJogadorRota(@RequestParam Rota rota){
        List<Jogador> jogadores = jogadorService.getJogadorByRota(rota);
        return ResponseEntity.ok(jogadores);
    }
    @GetMapping("/nickname/{nickname}")
    public ResponseEntity<Jogador> getJogadorNickname(@RequestParam String nickname){
        return ResponseEntity.ok(jogadorService.getJogadorByNickname(nickname));
    }

    @PostMapping
    public ResponseEntity<Jogador> postJogador(@RequestBody Jogador jogador){
        return ResponseEntity.ok(jogadorService.createJogador(jogador));
    }
    @PostMapping("/lote")
    public ResponseEntity<List<Jogador>> postJogador(@RequestBody List<Jogador> jogador){
        return ResponseEntity.ok(jogadorService.createJogadores(jogador));
    }
    @PatchMapping("/lote")
    public ResponseEntity<List<Jogador>> updateJogadores(@RequestBody List<Jogador> jogadores){
        return ResponseEntity.ok(jogadorService.updateJogadoresInLoteByNickname(jogadores));
    }
}
