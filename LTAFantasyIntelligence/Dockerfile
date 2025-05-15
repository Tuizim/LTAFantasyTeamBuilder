# Use uma imagem base com Python e uvicorn
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de dependências
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação
COPY . /app

# Exponha a porta que o uvicorn vai usar
EXPOSE 8000

# Comando para rodar a aplicação com uvicorn
CMD ["uvicorn", "app.controller.api:app", "--host", "0.0.0.0", "--port", "8000"]
