def import_converter(str_input):
    list_clean = list(map(str.strip, str_input.strip(
        '][').replace("'", "").split(',')))
    return list_clean


def input_reader():
    a = input()
    a = import_converter(a)
    b = input()
    b = import_converter(b)
    return a, b


def main():
    urls, commands = input_reader()
    for url in urls:
        for command in commands:
            if command == "rm -rf /":
                print(
                    f"На хосте {url} была попытка выполнить команду rm -rf / , но процесс выполнения был аварийно остановлен.")
                break
            print(f"На хосте {url} была выполнена команда {command}")
        else:
            continue
        break


if __name__ == '__main__':
    main()
