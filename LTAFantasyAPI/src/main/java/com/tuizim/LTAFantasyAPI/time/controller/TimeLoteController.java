package com.tuizim.LTAFantasyAPI.time.controller;

import com.tuizim.LTAFantasyAPI.time.model.Time;
import com.tuizim.LTAFantasyAPI.time.service.TimeService;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("times/lote")
@RequiredArgsConstructor
@Tag(name = "Times em Lote", description = "Operação de criação em massa")
public class TimeLoteController {
    private final TimeService timeService;

    @PostMapping()
    public ResponseEntity<List<Time>> adicionarTimeLote(@RequestBody List<Time> times) {
        return ResponseEntity.ok(timeService.criarTimeLote(times));
    }

}
