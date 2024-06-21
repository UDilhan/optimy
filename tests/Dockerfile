# Utiliser une image de base avec Python
FROM python:3.9-slim

# Installer les dépendances nécessaires
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    wget \
    gnupg2 \
    && rm -rf /var/lib/apt/lists/*

# Télécharger et installer Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Télécharger et installer le driver Chrome
RUN wget -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.63/linux64/chromedriver-linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip

# Configurer l'affichage pour que Chrome puisse s'exécuter sans tête
ENV DISPLAY=:99

# Copier le fichier de script dans l'image
COPY test_selenium.py /usr/src/app/test_selenium.py

# Installer Selenium
RUN pip install selenium

# Définir le répertoire de travail
WORKDIR /usr/src/app

# Commande par défaut pour exécuter le script
CMD ["python", "test_selenium.py"]
