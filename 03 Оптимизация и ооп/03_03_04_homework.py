# Если вы не использовали модуль collections 
# при решении задачи с подсчётом частот из предыдущего блока - 
# используйте этот модуль и его структуры для подсчёт частот.
if __name__ == '__main__':
    rps_values = (5081, '17184', 10968, 9666, '9102', 12321, '10617', 11633, 5035, 9554, '10424', 9378, '8577', '11602', 14116, '8066', '11977', '8572', 9685, 11062, '10561', '17820', 16637, 5890, 17180, '17511', '13203', 13303, '7330', 7186,
                  '10213', '8063', '12283', 15564, 17664, '8996', '12179', '13657', 15817, '16187', '6381', 8409, '5177', 17357, '10814', 6679, 12241, '6556', 12913, 16454, '17589', 5292, '13639', '7335', '11531', '14346', 7493, 15850, '12791', 11288)

    corrected_rps_values = list(map(int, rps_values))
    split_option = None

    while True:
        input_data = input("введите rps:")
        if input_data.isdigit():
            corrected_rps_values.append(int(input_data))
        elif ";" in input_data:
            corrected_rps_values.extend(map(int, input_data.split(";")))
        elif input_data == "":
            break
        elif "," in input_data:
            split_option = list(map(int, input_data.split(",")))
            print(
                f"делаем срез от {split_option[0]} до {split_option[1]} элемента")
            corrected_rps_values = corrected_rps_values[split_option[0]:
                                                        split_option[1]]

            break
        else:
            print('validation not passed')
    corrected_rps_values.sort()
    print(corrected_rps_values)

    quotient, remainder = divmod(len(corrected_rps_values), 2)
    median = corrected_rps_values[quotient] if remainder else sum(
        corrected_rps_values[quotient - 1:quotient + 1]) / 2

    # сбор информации по частоте и среднему
    rps_hist = {}
    sum_of_rps = 0
    for rps in corrected_rps_values:
        rps_coun = rps_hist.get(rps)
        if rps_coun is None:
            rps_hist[rps] = 0
        rps_hist[rps] += 1
        sum_of_rps += rps
    mean_rps = sum_of_rps/len(corrected_rps_values)

    # сортировка частот
    for w in sorted(rps_hist, key=rps_hist.get, reverse=True):
        print(w, rps_hist[w])
    
    direction = mean_rps/median - 1

    if direction > 0.3:
        direction_string = "Снижения"
    elif direction < -0.3:
        direction_string = "Скачки"
    else:
        direction_string = "Стабильная"

    print(f"{mean_rps//1:.0f}, {median:.0f}, {direction_string}")
