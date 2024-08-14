def count_letters(letter, input_word):
    # TODO: Retorne o número de letras (letter) no texto informado (string)
    # ou 0 caso não haja nenhuma correspodência
    count = 0
    for item in input_word:
        if item == letter:
            count +=1
    return count
