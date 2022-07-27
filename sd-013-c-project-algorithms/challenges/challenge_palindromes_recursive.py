def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if len(word) == 0:
        return False
    controle = True
    wordPalidromo = word[-1]
    wordSlice = word[0:high_index]
    wordNormal = word[low_index]
    if wordPalidromo != wordNormal:
        return False
    if low_index+1 < len(word)/2:
        test = is_palindrome_recursive(
            wordSlice, low_index + 1, len(wordSlice)-1)
        if test is False:
            controle = False

    return controle


teste = "abxzba"

print(is_palindrome_recursive(teste, 0, len(teste)-1))
