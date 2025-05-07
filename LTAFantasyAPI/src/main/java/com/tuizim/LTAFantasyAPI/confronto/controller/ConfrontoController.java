package com.tuizim.LTAFantasyAPI.confronto.controller;

import com.tuizim.LTAFantasyAPI.confronto.model.Confronto;
import com.tuizim.LTAFantasyAPI.confronto.service.ConfrontoService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("confrontos")
@RequiredArgsConstructor
public class ConfrontoController {
    private final ConfrontoService confrontoService;
    @PostMapping()
    public ResponseEntity<Confronto> criarConfronto(@RequestBody Confronto confronto){
        return ResponseEntity.ok(confrontoService.criarConfronto(confronto));
    }

    @DeleteMapping()
    public ResponseEntity<String> deletarConfronto(@RequestBody Confronto confronto){
        return ResponseEntity.ok(confrontoService.apagarConfronto(confronto));
    }
    @GetMapping
    public ResponseEntity<List<Confronto>> buscarConfrontos(){
        return ResponseEntity.ok(confrontoService.buscarConfrontos());
    }
}
