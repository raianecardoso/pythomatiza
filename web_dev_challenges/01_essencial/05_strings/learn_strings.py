def has_letter(letter, input_word):
    # TODO: Retorne True ou False para a existência da letra (letter) no texto informado (string)
    if letter in input_word:
        return True
    else:
        return False

def uper_case(input_word):
    # TODO: Retorne o valor to texto todo em letras maiúsculas
    return input_word.upper()

def lower_case(input_word):
    # TODO: Retorne o valor to texto todo em letras minúsculas
    return input_word.lower()

def capitalize(input_word):
    # TODO: Retorne o valor to texto todo com a primeira letra maiúscula
    return input_word.capitalize()

def reverse(input_word):
    # TODO: Retorne o valor inverso de um texto
    return(input_word[::-1])
