#Version pour comprendre docker 

FROM python:3.11-slim

#Crée un dossier /app et va dedans
WORKDIR /app

#Installe tous les librairies
RUN pip install numpy

# Copie tout  code
COPY . .

# Ouvre la porte 8501 pour accéder à l'app
EXPOSE 8501

# Lance application
CMD ["python", "Tp2.py"]

