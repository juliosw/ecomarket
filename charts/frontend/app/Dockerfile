# Usa uma imagem base Python leve
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos da aplicação
COPY main.py .

# Instala as dependências necessárias
RUN pip install fastapi httpx uvicorn

# Expõe a porta 8000 (usada pelo FastAPI)
EXPOSE 8000

# Define o comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
