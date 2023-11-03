#
# Test Google v1.0.0
# Autor Diogo Hidalgo Daia
#

# Importes
import Log
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

log = Log.get_logger(__name__)

def pesquisar_google(driver:WebDriver , texto_pesquisa):
    try:
        form = driver.find_element(By.TAG_NAME , 'form')
        form.find_element(By.TAG_NAME , 'textarea').send_keys(texto_pesquisa)
        time.sleep(2)
        form.find_element(By.TAG_NAME , 'input').click()
        time.sleep(5)
    except Exception as e:
        log.error(f'Erro ao pesquisar no google')
        log.error(f'ERROR -> {e}')

def primeiro_resultado(driver:WebDriver):
    try:
        search = driver.find_element(By.ID , 'search')
        result_1 = search.find_element(By.TAG_NAME , 'h3').text
        log.info(f'texto do primeiro resultado: {result_1}')
        search.find_element(By.TAG_NAME , 'h3').click()
        time.sleep(5)
    except Exception as e:
        log.error(f'Erro ao selecionar o primeiro resultado')
        log.error(f'ERROR -> {e}')
