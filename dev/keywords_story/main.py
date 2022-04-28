from get_keywords import get_keywords


def main():
    with open("data.txt", "r", encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            print(line, get_keywords(line))


if __name__ == '__main__':
    main()
