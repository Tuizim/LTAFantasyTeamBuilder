package com.tuizim.LTAFantasyAPI.util;

import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.databind.DeserializationContext;
import com.fasterxml.jackson.databind.JsonDeserializer;

import java.io.IOException;

public class StringToDoubleDeserializer extends JsonDeserializer<Double> {

    @Override
    public Double deserialize(JsonParser p, DeserializationContext ctxt) throws IOException {
        String value = p.getText();
        try {
            return Double.parseDouble(value);
        } catch (NumberFormatException e) {
            return 0.0; // ou lançar erro, ou null se usar Double (objeto)
        }
    }
}
