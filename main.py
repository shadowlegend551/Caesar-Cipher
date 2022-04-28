from tokenizer import tokenize
from parser import parse
from translator import translate


def main():
    while True:
        totokenize = input('$~ ')
        tokenized = tokenize(totokenize)
        parsed = parse(tokenized)
        translated = translate(parsed)
        print(translated)


if __name__ == '__main__':
    main()