FROM python:3.11-slim

# Instala dependências do sistema pro Playwright
RUN apt-get update && apt-get install -y \
    libnss3 libatk-bridge2.0-0 libxss1 libasound2 libxshmfence1 libgbm1 libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/*

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos
COPY . .

# Instala as libs do Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Instala navegadores do Playwright
RUN playwright install --with-deps

# Comando padrão
CMD ["python", "main.py"]
