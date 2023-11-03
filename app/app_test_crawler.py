#
# Crawler Tester v1.0.0
# Autor Diogo Hidalgo Daia
#

# Importes
import Log
import Configs
import Crawler
import Files
import time
import test_google as goo

log = Log.get_logger(__name__)

def main(browser_configs):
    try:
        log.info(f'Iniciando projeto de teste do crawler')
        start_time = Log.time_now()
        
        log.info(f'Criando pastas do projeto')
        Files.create_dir(Configs.get_download_configs()['download_path'])

        log.info(f'Iniciando o driver do chrome')
        driver = Crawler.open_chrome_browser(browser_configs)

        log.info(f'Mudando para a pagina do google')
        Crawler.change_page(driver , Configs.get_configs('URLS')['url_padrao'])
        time.sleep(3)

        log.info(f'Executando teste de pesquisa no google')
        texto_pesquisa = f'o que é um webcrawler'
        goo.pesquisar_google(driver , texto_pesquisa)

        log.info(f'Abrindo primeiro resultado da busca')
        goo.primeiro_resultado(driver)
    except Exception as e:
        log.error(f'Erro no teste de Crawler')
        log.error(f'ERROR -> {e}')
        exit(1)
    finally:
        execution_time = Log.execution_time(start_time)
        log.info(f'Tempo total de execução: {execution_time:0.2f} segundos')
        log.info(f'Processo Finalizado')

if __name__ == "__main__":
    main(
        Configs.get_browser_configs()
    )