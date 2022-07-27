# referencia: https://www.delftstack.com/pt/howto/
# python/find-max-value-in-dictionary-python/
import csv
import os


def analyze_log(path_to_file):
    stringGravar = read(path_to_file)
    gravar(stringGravar)


def read(path):
    pratosJoaoComeu = set()
    diasJoaoFoi = set()
    todosPratos = set()
    todosdias = set()
    if not path.endswith('.csv'):
        raise FileNotFoundError(f'Extensão inválida: {path}')

    if not os.path.isfile(path):
        raise FileNotFoundError(f'Arquivo inexistente: {path}')

    with open(path) as file:
        file_csv = list(csv.reader(file))
        for linha in file_csv:
            todosPratos.add(linha[1])
            todosdias.add(linha[2])
            if linha[0] == "joao":
                pratosJoaoComeu.add(linha[1])
                diasJoaoFoi.add(linha[2])
        maisPedidoMaria = maria(file_csv)
        vezesArnaldoHamburguer = arnaldo(file_csv)

    return(
            f'{max(maisPedidoMaria, key=lambda key: maisPedidoMaria[key])}\n'
            f'{vezesArnaldoHamburguer}\n{todosPratos - pratosJoaoComeu}\n'
            f'{todosdias - diasJoaoFoi}\n'
    )


def arnaldo(file_csv):
    vezesArnaldoHamburguer = 0
    for linha in file_csv:
        if linha[0] == "arnaldo" and linha[1] == 'hamburguer':
            vezesArnaldoHamburguer += 1
    return vezesArnaldoHamburguer


def maria(file_csv):
    maisPedidoMaria = dict()
    for linha in file_csv:
        if linha[0] == "maria":
            if linha[1] in maisPedidoMaria:
                maisPedidoMaria[linha[1]] += 1
            else:
                maisPedidoMaria[linha[1]] = 1
    return maisPedidoMaria


def gravar(stringGravar):
    fileName = "data/mkt_campaign.txt"
    with open(fileName, 'w') as file:
        file.write(stringGravar)
