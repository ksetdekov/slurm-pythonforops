def input_rps():
    input_str = input("введите rps:")
    if input_str == "":
        print('ввод прерван')
        return None
    return input_str


def modify_rps_list_with_input_data(input_str, rps_list):
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


def calculate_direction(mean, median):
    direction = mean / median - 1
    if direction > 0.3:
        directions_result = "Снижения"
    elif direction < -0.3:
        directions_result = "Скачки"
    else:
        directions_result = "Стабильная"
    return directions_result


def print_hist_data(hist_to_print):
    for w in sorted(hist_to_print, key=hist_to_print.get, reverse=True):
        print(w, hist_to_print[w])


def calculate_median(list_of_values):
    quotient, remainder = divmod(len(list_of_values), 2)
    median = list_of_values[quotient] if remainder else sum(
        list_of_values[quotient - 1:quotient + 1]) / 2
    return median


def calculate_hist_mean_median(list_of_ints):
    mean, hist = calculate_hist_and_mean(list_of_ints)
    median = calculate_median(list_of_ints)
    return mean, hist, median


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
        rps_values, break_option = modify_rps_list_with_input_data(input_str=input_data, rps_list=corrected_rps_values)
        if break_option is not None:
            break

    corrected_rps_values.sort()
    print("вот список упорядоченных rps")
    print(corrected_rps_values)

    # сбор информации по частоте, среднему и медиане
    mean_rps, rps_hist, median_rps = calculate_hist_mean_median(corrected_rps_values)

    # сортировка частот и вывод частот
    print("вот частота значений rps")
    print_hist_data(rps_hist)

    #  расчет направления движения и вывод результата
    direction_string = calculate_direction(mean_rps, median_rps)
    print("среднее, медиана, направление движения:")
    print(f"{mean_rps // 1:.0f}, {median_rps:.0f}, {direction_string}")
