package com.tuizim.LTAFantasyAPI.config;

public final class ErrorMessages {
    private ErrorMessages() {}
    public static final String JOGADOR_NOTFOUND_ID =
            "Jogador com id %d não encontrado";
    public static final String JOGADOR_NOTFOUND_NICKNAME =
            "Jogador com nickname '%s' não encontrado";
    public static final String JOGADOR_INVALID_PARAMS =
            "É preciso informar id ou nickname";
    public static final String JOGADOR_JUST_EXISTS =
            "Jogador com este nickname já está cadastrado";
    public static final String TIME_JUST_EXISTS =
            "Time com este nome já está cadastrado";
    public static final String TIME_NOTFOUND_NOME =
            "Time com nome %s não foi encontrado";
    public static final String CONFRONTO_JUST_EXISTS =
            "Este confronto já está cadastrado";
    public static final String CONFRONTO_NOT_EXISTS =
            "Este confronto não existe";
    public static final String CONFRONTO_IT_SELF_ERROR =
            "Time não pode jogar contra ele mesmo";
    public static final String TIME_VITORIOSO_INVALID =
            "Time vitorioso está invalido";
}
