# Utiliser une image Python officielle
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt ./
COPY app.py ./
COPY personnalites.csv ./
COPY templates ./templates
COPY static ./static


# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port par défaut de Flask
EXPOSE 5000

# Lancer l'application
CMD ["python", "app.py"]
