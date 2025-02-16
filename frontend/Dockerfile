# Usar uma imagem base do Nginx para servir o frontend
FROM nginx:alpine

# Copiar o arquivo HTML para o diretório de conteúdo do Nginx
COPY index.html /usr/share/nginx/html/index.html

# Expor a porta 80
EXPOSE 80

# O Nginx já inicia automaticamente, então não precisamos de um CMD