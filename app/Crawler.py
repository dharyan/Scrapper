#
# Crawler v1.0.0
# Autor Diogo Hidalgo Daia
#

# Importes
import Log
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
import time

log = Log.get_logger(__name__)

def open_chrome_browser(browser_configs):
    try:
        chromeOptions = webdriver.ChromeOptions()
        
        for argument in browser_configs['chorme_arguments']:
            if browser_configs['chorme_arguments'][argument] == "True":
                if argument == 'headless':
                    chromeOptions.add_argument('headless=new')
                else:
                    chromeOptions.add_argument(f'--{argument.strip()}')

        chrome_size_parm = list(browser_configs['chrome_size'].keys())[0]
        chrome_size = browser_configs['chrome_size'][chrome_size_parm]
        chromeOptions.add_argument(f'--{chrome_size_parm}={chrome_size}')

        chromeOptions.add_experimental_option("prefs",browser_configs['chromeOptions_prefs'])
        driver = webdriver.Chrome(
            service = Service(ChromeDriverManager().install()),
            options = chromeOptions
        )
        return driver
    except Exception as e:
        log.error(f'Erro ao abrir o browser do chrome')
        log.error(f'ERROR -> {e}')
        exit(1)

def close_browser(driver:WebDriver):
    try:
        driver.quit()
    except Exception as e:
        log.error(f'Erro ao fechar o browser')
        log.error(f'ERROR -> {e}')
        exit(1)

def change_page(driver:WebDriver,url):
    try:
        log.info(f"Mudando para pagina - {url}")
        driver.get(url)
        time.sleep(1)
    except Exception as e:
        log.error(f'Erro ao mudar de pagina')
        log.error(f'ERROR -> {e}')
        exit(1)
