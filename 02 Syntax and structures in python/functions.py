def input_rps():
    """захват ввода данных

    :return: введенные значения или None, если ничего не ввели
    :rtype: str
    """
    input_str = input("введите rps:")
    if input_str == "":
        print('ввод прерван')
        return None
    return input_str


def modify_rps_list_with_input_data(input_str, rps_list):
    """получаем входные данные и список rps и модифицируем список рпс, 
    добавляя или по одному значения или много. Также выдаем значение True 
    на 1 позиции в tuple, если нужно прервать цикл ввода

    :param input_str: строка ввода
    :type input_str: str
    :param rps_list: список из int
    :type rps_list: list
    :return: tuple из списка с дополнеными значениями и True или None в зависимости от того, нужно ли прерывать цикл
    :rtype: (list, bool)
    """
    break_command = None
    if input_str is None:
        break_command = True
    elif input_str.isdigit():
        rps_list.append(int(input_str))
    elif ";" in input_str:
        rps_list.extend(map(int, input_str.split(";")))
    elif "," in input_str:
        split_option = list(map(int, input_str.split(",")))
        print(
            f"делаем срез от {split_option[0]} до {split_option[1]} элемента")
        rps_list = rps_list[split_option[0]:split_option[1]]
        break_command = True
    else:
        print('validation not passed')

    return rps_list, break_command


def calculate_hist_and_mean(list_of_values):
    """расчет гистограммы и среднего для списка

    :param list_of_values: список чисел
    :type list_of_values: list
    :return: значение среднего и словарь частот
    :rtype: (float, dict)
    """
    hist = {}
    sum_of_rps = 0
    for rps in list_of_values:
        count = hist.get(rps)
        if count is None:
            hist[rps] = 0
        hist[rps] += 1
        sum_of_rps += rps
    mean = sum_of_rps / len(list_of_values)
    return mean, hist


def print_hist_data(hist_to_print):
    """сортировка словаря с гистограммой по частоте и распечатка его

    :param hist_to_print: словарь, где значения - частота
    :type hist_to_print: dict
    """    
    for w in sorted(hist_to_print, key=hist_to_print.get, reverse=True):
        print(w, hist_to_print[w])


def calculate_median(list_of_values):
    """расчет медианы из списка

    :param list_of_values: список значений
    :type list_of_values: list
    :return: значение медианы
    :rtype: float
    """    
    quotient, remainder = divmod(len(list_of_values), 2)
    median = list_of_values[quotient] if remainder else sum(
        list_of_values[quotient - 1:quotient + 1]) / 2
    return median


def calculate_hist_mean_median(list_of_ints):
    """запуск для одного списка расчета среднего, медианы и частоты значений

    :param list_of_ints: список значений
    :type list_of_ints: list
    :return: tuple из среднего, гисограммы и медианы
    :rtype: (float, float, float)
    """    
    mean, hist = calculate_hist_and_mean(list_of_ints)
    median = calculate_median(list_of_ints)
    return mean, hist, median


def calculate_direction(mean, median):
    """решение задачи сравнения среднего и медианы

    :param mean: среднее
    :type mean: float
    :param median: медиаана
    :type median: float
    :return: строка результата сравнения
    :rtype: str
    """
    direction = mean / median - 1
    if direction > 0.3:
        directions_result = "Снижения"
    elif direction < -0.3:
        directions_result = "Скачки"
    else:
        directions_result = "Стабильная"
    return directions_result


if __name__ == '__main__':
    rps_values = (5081, '17184', 10968, 9666, '9102', 12321, '10617', 11633, 5035, 9554, '10424', 9378, '8577', '11602',
                  14116, '8066', '11977', '8572', 9685, 11062, '10561', '17820', 16637, 5890, 17180, '17511', '13203',
                  13303, '7330', 7186, '10213', '8063', '12283', 15564, 17664, '8996', '12179', '13657', 15817, '16187',
                  '6381', 8409, '5177', 17357, '10814', 6679, 12241, '6556', 12913, 16454, '17589', 5292, '13639',
                  '7335', '11531', '14346', 7493, 15850, '12791', 11288)

    corrected_rps_values = [int(value) for value in rps_values]

    while True:
        # read input
        input_data = input_rps()
        # procecc input
        rps_values, break_option = modify_rps_list_with_input_data(
            input_str=input_data, rps_list=corrected_rps_values)
        if break_option is not None:
            break

    corrected_rps_values.sort()
    print("вот список упорядоченных rps")
    print(corrected_rps_values)

    # сбор информации по частоте, среднему и медиане
    mean_rps, rps_hist, median_rps = calculate_hist_mean_median(
        corrected_rps_values)

    # сортировка частот и вывод частот
    print("вот частота значений rps")
    print_hist_data(rps_hist)

    #  расчет направления движения и вывод результата
    direction_string = calculate_direction(mean_rps, median_rps)
    print("среднее, медиана, направление движения:")
    print(f"{mean_rps // 1:.0f}, {median_rps:.0f}, {direction_string}")
