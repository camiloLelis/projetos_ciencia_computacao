import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for i in range(len(instance)):
        file = instance.search(i)
        if file["nome_do_arquivo"] == path_file:
            return None
    arrayLine = txt_importer(path_file)
    stringReturn = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(arrayLine),
        "linhas_do_arquivo": arrayLine
    }
    instance.enqueue(stringReturn)

    # print(stringReturn, file=sys.stdout)
    sys.stdout.write(str(stringReturn))


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) > 0:
        path_file = instance.dequeue()
        print(
                f'Arquivo {path_file["nome_do_arquivo"]} removido com sucesso',
                file=sys.stdout
            )
    else:
        print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        data = instance.search(position)
        print(data, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
