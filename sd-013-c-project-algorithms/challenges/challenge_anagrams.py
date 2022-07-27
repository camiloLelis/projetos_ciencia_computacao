def is_anagram(first_string, second_string):
    if (insertion_sort(first_string) == insertion_sort(second_string)):
        return True
    return False


def insertion_sort(string):
    array = list(string.lower())
    for i in range(len(array)):
        current_value = array[i]
        current_position = i
        # enquanto o valor da posição for menor que os elementos a sua esquerda
        while (
            current_position > 0
            and array[current_position - 1] > current_value
        ):
            # move as posições para a direita
            array[current_position] = array[current_position - 1]
            current_position = current_position - 1
            # colocamos o elemento em sua nova posição
        array[current_position] = current_value
    return ''.join(array)
# https://app.betrybe.com/course/computer-science/algoritmos/algoritmos-de-ordenacao-e-busca/29521083-44ea-488d-a74d-216b1ac79b04/conteudos/766d59bd-a04f-41a9-b41b-5fb37a2f2a3a/algoritmos-de-ordenacao/1adc1a6e-51c7-4065-ae2c-e5f8194e7578?use_case=next_button


"""

def is_anagram(first_string):
    if len(first_string) == 0:
      return False
    x = first_string
    string_montada = ""
    while len(first_string) > 1:
        first_inicio = first_string[0]
        first_cort = first_string[1:]
        tamanho = len(first_string)
        cort_inicio = first_cort[0]
        if cort_inicio.lower() > first_inicio.lower():
            first_string = first_cort
            string_montada = string_montada + first_inicio

        else:
            first_string = first_inicio + first_cort[1:]
            string_montada = string_montada + cort_inicio


    is_anagram(string_montada)
    print(first_string)


    return first_string
is_anagram("dcvbxxxaassallla")

"""
