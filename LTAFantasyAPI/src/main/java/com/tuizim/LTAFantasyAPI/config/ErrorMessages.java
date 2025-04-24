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
}
