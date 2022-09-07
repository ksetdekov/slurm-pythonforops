if __name__ == '__main__':
    last_humidity = None
    while last_humidity is None:
        print("Введите влажность (целое число)")
        input_data = input()
        if input_data.isdigit():
            last_humidity = int(input_data)

    workroom_humidity = (42, 46, 39, 47, 53, 58, 52, 53, 48, last_humidity)

    sum_of_humidity = 0
    for humidity in workroom_humidity:
        sum_of_humidity += humidity

    for i in range(1, 6, 2):
        print(i, sum_of_humidity / len(workroom_humidity))
