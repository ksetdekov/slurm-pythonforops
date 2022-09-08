
def work_with_mutables(my_list):
    my_list[2].append(10)


def main():
    my_pretty_list = (1, 2, [3, 4, 5])
    # изменит список, даже если внутри неизменяемого типа данных
    work_with_mutables(my_pretty_list)
    print(my_pretty_list)


if __name__ == '__main__':
    main()
