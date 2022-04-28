def tokenize(Input):
    tokenized = []
    currenttoken = ''
    file = open('opers.txt', 'r')
    breakpoints = file.read().split('.')
    file.close()

    for char in Input:
        if char in breakpoints:
            if currenttoken != '':
                tokenized.append(currenttoken)
                currenttoken = ''
            tokenized.append(char)
        elif char == ' ':
            if currenttoken != '':
                tokenized.append(currenttoken)
                currenttoken = ''
        else:
            currenttoken += char

    if currenttoken != '':
        tokenized.append(currenttoken)
    return tokenized
