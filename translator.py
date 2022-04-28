def translate(parsed):
    errorcode = '\u001b[31m'  # Red
    resetcode = '\u001b[0m'  # Console's default colour.

    if isinstance(parsed, str):
        return parsed

    charactersetsourcefile = 'charsets.txt'
    charsetname = 'default'
    tofile = None
    text = None
    translated = ''
    key = None

    for part in parsed:
        if part[0] == '"':
            text = list(part[1].lower())


        elif part[0] == '<' or part[0] == '>':
            try:
                key = int(part[1])
            except ValueError:
                return f"{errorcode}Parameter 'Key' must be type 'Int'{resetcode}"
            if part[0] == '>':
                key *= -1  # Decoding goes left.


        elif part[0] == '?':
            key = 0


        elif part[0] == '&':
            charsetname = part[1]


        elif part[0] == '*':
            tag = f'<{part[1]}>'
            contents = part[2]
            file = open('charsets.txt', 'a')
            file.write(f'{tag}{contents.lower()}{tag}')
            file.close()


        elif part[0] == '#':
            try:
                file = open(part[1], 'r')
            except FileNotFoundError:
                return f'{errorcode}File to read not found{resetcode}'
            text = list(file.read())
            file.close()


        elif part[0] == '@':
            tofile = part[1]

    file = open(charactersetsourcefile, 'r')  # Get charset.
    try:
        charset = list(file.read().split(f'<{charsetname}>')[1])
    except IndexError:
        return f"{errorcode}Charset does not exist{resetcode}"

    charset += charset
    file.close()

    if key is not None and key == 0:  # If operation is full.
        if text is None:
            return f"{errorcode}Parameter 'Text' has no value{resetcode}"
        for j in range(int(len(charset) / 2)):
            for i in range(len(text)):
                text[i] = (lambda a, b, c: a[a.index(b) + c] if b in a else b)(charset, text[i], 1)
            translated += ''.join(text) + '\n'


    elif key is not None:
        if text is None:
            return f"{errorcode}Parameter 'Text' has no value{resetcode}"
        while len(charset) < key:
            key -= len(charset)  # Removes redundant length from key.
        for i in range(len(text)):
            text[i] = (lambda a, b, c: a[a.index(b) + c] if b in a else b)(charset, text[i], key)
        translated += ''.join(text)

    if tofile is not None:
        file = open(tofile, 'w')
        file.write(translated)

    return translated