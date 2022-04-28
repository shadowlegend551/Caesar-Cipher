def parse(tokenized):
    errorcode = '\u001b[31m'
    resetcode = '\u001b[0m'

    parsed = []

    file = open('opers.txt', 'r')
    file_read = file.read()
    file.close()
    actions = file_read.split('.')[:5]

    while len(tokenized) > 0:
        temp = []
        temp.append(tokenized.pop(0))  # operation

        if temp[0] in actions:
            try:
                temp.append(tokenized.pop(0))
            except IndexError:
                return f"{errorcode}Value for '{temp[0]}' not given{resetcode}"

        elif temp[0] == '*':
            tempstr = []
            try:
                temp.append(tokenized.pop(0))
            except IndexError:
                return f"{errorcode}Parameter 'Charsetname' not given{resetcode}"
            try:
                del tokenized[0]
                while tokenized[0] != '"':
                    tempstr.append(tokenized.pop(0))
                temp.append(' '.join(tempstr))
                del tokenized[0]
            except IndexError:
                return f"{errorcode}Parameter 'Charset' not given/given improperly{resetcode}"

        elif temp[0] == '"':
            tempstr = []
            try:
                while tokenized[0] != '"':
                    tempstr.append(tokenized.pop(0))
                temp.append(' '.join(tempstr))
                del tokenized[0]
            except IndexError:
                return f'{errorcode}Unpaired quotes{resetcode}'

        parsed.append(temp)
    return parsed