#
# Configs v1.0.0
# Autor Diogo Hidalgo Daia
#

# Importes
import configparser
import Log

log = Log.get_logger(__name__)

def get_env_configs():
    try:
        config = configparser.ConfigParser(interpolation=None)
        config.read('.settings.ini')
        return {s:dict(config.items(s)) for s in config.sections()}
    except Exception as e:
        log.error(f'ERROR -> {e}')
        exit(1)

def get_browser_configs():
    try:
        config = get_env_configs()
        config['CHROME_OPTIONS']['download.default_directory'] = get_download_configs()['download_path']
        browser_configs = {
            "chromeOptions_prefs":config['CHROME_OPTIONS'],
            "chorme_arguments":config['CHORME_ARGUMENTS'],
            "chrome_size":config['CHROME_SIZE']
        }
        return browser_configs
    except Exception as e:
        log.error(f'ERRROR -> {e}')
        exit(1)

def get_download_configs():
    try:
        config = get_env_configs()
        return config['DOWNLOAD']
    except Exception as e:
        log.error(f'ERRROR -> {e}')
        exit(1)

def get_configs(tag):
    try:
        config = get_env_configs()
        return config[tag]
    except Exception as e:
        log.error(f'ERRROR -> {e}')
        exit(1)
