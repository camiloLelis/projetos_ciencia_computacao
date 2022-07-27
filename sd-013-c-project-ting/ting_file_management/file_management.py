import sys


def txt_importer(path_file):
    """Aqui irá sua implementação teste"""
    if not path_file.endswith('.txt'):
        print("Formato inválido", file=sys.stderr)

    try:
        with open(path_file) as file:
            file_txt = file.readlines()
            array_new = list()
            for linha in file_txt:
                array_new.append(linha.strip())
        return array_new
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
