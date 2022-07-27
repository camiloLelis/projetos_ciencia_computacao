from ting_file_management.file_process import process
from ting_file_management.queue import Queue


def exists_word(word, instance):
    """Aqui irá sua implementação"""
    arrayOcorrencia = list()
    for i in range(len(instance)):
        file = instance.search(i)
        ocorrencias = list()
        for i, linha in enumerate(file["linhas_do_arquivo"]):
            if linha.lower().find(word.lower()) != -1:
                ocorrencias.append({"linha": i + 1})
        ocorr = {
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": ocorrencias
        }
        if len(ocorrencias) > 0:
            arrayOcorrencia.append(ocorr)
    return arrayOcorrencia


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    arrayOcorrencia = list()
    return arrayOcorrencia


if __name__ == "__main__":
    project = Queue()
    process("statics/nome_pedro.txt", project)
    process("statics/nome_pedro2.txt", project)

    print("__________________________________________")
    print(exists_word("teste", project))
