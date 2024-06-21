from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys
import time

if len(sys.argv) != 2:
    print("Usage: python test_selenium.py <URL>")
    sys.exit(1)

url = sys.argv[1]

# Configuration des options de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialisation du driver Chrome
driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)

try:
    # Accéder à l'URL
    driver.get(url)
    time.sleep(3)
    
    # Vérifier que les données de la table 'test' sont affichées
    assert "test1" in driver.page_source
    assert "test2" in driver.page_source
    assert "test3" in driver.page_source

    print("Test réussi : les données de la table 'test' sont affichées correctement.")
except AssertionError:
    print("Test échoué : les données de la table 'test' ne sont pas affichées correctement.")
except Exception as e:
    print(f"Le site {url} n'est pas accessible. Erreur : {e}")
finally:
    # Fermer le driver
    driver.quit()
