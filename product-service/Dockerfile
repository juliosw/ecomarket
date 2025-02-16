# Usar uma imagem base do Go
FROM golang:1.19-alpine

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo go.mod e go.sum para o container
COPY go.mod .
COPY go.sum .

# Baixar as dependências do Go
RUN go mod download

# Copiar o código-fonte para o container
COPY . .

# Compilar o aplicativo
RUN go build -o product-service .

# Expor a porta que o serviço vai rodar
EXPOSE 8080

# Comando para executar o aplicativo
CMD ["./product-service"]