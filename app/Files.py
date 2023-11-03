#
# Files v1.0.0
# Autor Diogo Hidalgo Daia
#

# Importes
import os
import Log

log = Log.get_logger(__name__)

def rename_files(old_name,new_name):
    try:
        os.rename(old_name,new_name)
        log.info(f'Arquivo renomeado - {old_name} --> {new_name}')
    except Exception as e:
        log.error(f'Erro ao renomear o arquivo {old_name}')
        log.error(f'ERROR -> {e}')

def create_dir(folder_path):
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            log.info(f'Diretorio criado - {folder_path}')
    except Exception as e:
        log.error(f'Erro ao criar diretorio {folder_path}')
        log.error(f'ERROR -> {e}')

def remove_file_if_exists(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            log.info(f'Arquivo removido - {file_path}')
    except Exception as e:
        log.error(f'Erro ao remover arquivo {file_path}')
        log.error(f'ERROR -> {e}')

def move_file(current_folder,destination_folder):
    try:
        os.replace(current_folder,destination_folder)
        log.info(f'Arquivo movido - {current_folder} --> {destination_folder}')
    except Exception as e:
        log.error(f'Erro ao mover arquivo {current_folder}')
        log.error(f'ERROR -> {e}')

def empty_folder(folder_path):
    try:
        log.info(f'Removendo arquivos - {folder_path}')
        files_list = filter(os.path.isfile , os.listdir(folder_path))
        exception_list = [
            '.gitkeep'
        ]
        for file in files_list:
            if file.strip() in exception_list:
                continue
            remove_file_if_exists(f"{folder_path}/{file.strip()}")
    except Exception as e:
        log.error(f'Erro ao esvaziar pasta {folder_path}')
        log.error(f'ERROR -> {e}')
