#
# Scraper Tester v1.0.0
# Autor Diogo Hidalgo Daia
#

# Importes
import Log
import Configs
import Files
import time
import test_scraper as ts

log = Log.get_logger(__name__)

def main(browser_configs):
    try:
        log.info(f'Iniciando projeto de teste do crawler')
        start_time = Log.time_now()
        
        log.info(f'Criando pastas do projeto')
        Files.create_dir(Configs.get_download_configs()['download_path'])

        
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