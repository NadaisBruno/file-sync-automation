import os
from pathlib import Path  # biblioteca que torna o codigo mais legivel e facil de trabalhar com ficheiros e diretorios
import shutil  # biblioteca usada para copiar, mover e remover(neste caso nao usamos a funcao do shutil para remover pois e mais util para remover pastas inteiras que nao e o caso aqui)
from datetime import datetime
import time
import sys  # used to access command-line arguments


def log(mensagem, path_to_log):
    formato = "%d-%m-%Y %H:%M:%S"
    date_time = datetime.now().strftime(formato)
    print(f"{date_time} - {mensagem}")

    with open(path_to_log, "a", encoding="utf8") as file:
        file.write(f"{date_time} - {mensagem}\n")


def copy_files(p_source, p_replica, path_to_log):

    # iterar por cada item na pasta source e imprimir cada item(ficheiro)
    for item in p_source.iterdir():
        # so imprime ficheiros e nao apanha pastas, se lá existirem
        if item.is_file():
            print(item.name)  # imprime apenas o nome do ficheiro sem a pasta source neste caso

            # aqui definimos o caminho onde o ficheiro deve ficar
            replica_path = p_replica / item.name

            # se nao existir o ficheiro no path replica cria uma cópia entao desse ficheiro
            if not replica_path.exists():
                shutil.copy2(item, replica_path)
                log(f"File copied: {item}", path_to_log)


def remove_files(p_replica, p_source, path_to_log):
    for item in p_replica.iterdir():
        if item.is_file():

            # cria o caminho do ficheiro na pasta source com o mesmo nome
            # constroi o caminho equivalente na source para comparar se o ficheiro existe
            source_path = p_source / item.name

            # se nao existir o ficheiro no path source remove esse mesmo ficheiro do path replica
            if not source_path.exists():
                os.remove(item)
                log(f"File removed: {item.name}", path_to_log)


def main():
    # arguments

    if len(sys.argv) != 6:
        print("Expected 5 arguments.Exiting program")
        sys.exit()

    path_to_source = sys.argv[1]  # source folder // string recebida como argumento
    path_to_replica = sys.argv[2]  # replica folder
    interval = int(sys.argv[3])  # time between syncs in seconds
    amount_of_synchro = int(sys.argv[4])  # amount of cicles
    path_to_log = sys.argv[5]  # log file path

    # here we create the source path
    # objeto Path criado que permite trabalhar com ficheiros e diretorios de forma mais facil
    p_source = Path(path_to_source)
    if not p_source.exists():
        log(f"Source folder does not exist.Program is closing", path_to_log)
        sys.exit()

    # here we create the replica path
    p_replica = Path(path_to_replica)
    if not p_replica.exists():
        p_replica.mkdir()
        log(f"Creating replica folder", path_to_log)



    for i in range(amount_of_synchro):
        copy_files(p_source, p_replica, path_to_log)
        remove_files(p_replica, p_source, path_to_log)

        time.sleep(interval)


if __name__ == "__main__":
    main()
