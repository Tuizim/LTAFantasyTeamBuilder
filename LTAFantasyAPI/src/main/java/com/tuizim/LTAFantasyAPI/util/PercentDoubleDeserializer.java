package com.tuizim.LTAFantasyAPI.util;

import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.databind.DeserializationContext;
import com.fasterxml.jackson.databind.JsonDeserializer;

import java.io.IOException;

public class PercentDoubleDeserializer extends JsonDeserializer<Double> {
    @Override
    public Double deserialize(JsonParser p, DeserializationContext ctxt) throws IOException {
        String value = p.getText().replace("%", "").trim();
        try {
            return Double.parseDouble(value) / 100.0;
        } catch (NumberFormatException e) {
            return 0.0; // ou lançar exceção, se preferir
        }
    }
}
