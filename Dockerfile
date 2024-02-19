# Utilisez une image de base légère, par exemple, Alpine
FROM alpine:latest

# Définissez le répertoire de travail
WORKDIR /app

# Copiez les fichiers nécessaires dans le conteneur
COPY motd-api.py /app/

# Exposez le port sur lequel le microservice écoutera
EXPOSE 8080

# Commande pour exécuter le microservice
CMD ["python", "motd-api.py"]
