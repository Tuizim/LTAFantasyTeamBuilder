package com.tuizim.LTAFantasyAPI.time.controller;

import com.tuizim.LTAFantasyAPI.time.model.Time;
import com.tuizim.LTAFantasyAPI.time.service.TimeService;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("times")
@RequiredArgsConstructor
@Tag(name = "Times", description = "CRUD e buscas individuais de times")
public class TimeController {
    private final TimeService timeService;

    @GetMapping()
    public ResponseEntity<List<Time>> buscarTimes() {
        return ResponseEntity.ok(timeService.buscarTimes());
    }
    @GetMapping("/{nome}")
    public ResponseEntity<Time> buscarTimeNome(@PathVariable String nome) {
        return ResponseEntity.ok(timeService.buscarTimePorNome(nome));
    }
    @PostMapping()
    public ResponseEntity<Time> adicionarTime(@RequestBody Time time) {
        return ResponseEntity.ok(timeService.criarTime(time));
    }
    @DeleteMapping()
    public ResponseEntity<String> removerTime(@RequestParam String nome) {
        return ResponseEntity.ok(timeService.deletarTime(nome));
    }
}
