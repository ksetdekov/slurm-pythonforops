import json
from collections import deque


def extract_int(string):
    """из строки  в формате как в задании вытаскивает число

    :param string: строка с именем прокси
    :type string: str
    :return: число номера
    :rtype: int
    """    
    value = int(string.split("t")[1].split(".")[0])
    return value


def main():
    proxys = input()
    proxys = json.loads(proxys)
    # convert to ints
    proxys = [extract_int(i) for i in proxys]
    proxys_que = deque(proxys)
    print(proxys_que)
    print(len(proxys_que))

    # cycle
    for _ in range(1000):
        candidate = proxys_que.pop()
        print(f'Обращение при помощи прокси proxyhost{candidate}.slurm.io')

        if candidate % 3 == 0 or candidate % 8 == 0:
            continue
        print(
            f'Было осуществлено обращение к ресурсу при помощи прокси "proxyhost{candidate}.slurm.io"')
        proxys_que.appendleft(candidate)
    print(f'числ оставшихся в списке прокси {len(proxys_que)}')


if __name__ == '__main__':
    main()
