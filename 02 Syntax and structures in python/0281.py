if __name__ == '__main__':
    workroom_humidity = [42, 46, 39, 47, 53, 58, 52, 53, 48]

    while True:
        print("Введите влажность (целое число)")
        input_data = input()
        if input_data.isdigit():
            workroom_humidity.append(int(input_data))
        elif "," in input_data:
            workroom_humidity.extend(map(int, input_data.split(",")))
        elif input_data == "":
            break
        else:
            print('validation not passed')
    workroom_humidity.sort()
    print(workroom_humidity)
    outlier = workroom_humidity.pop()

    print(outlier)
    # origianl changed
    print(workroom_humidity)
    sum_of_humidity = 0
    for humidity in workroom_humidity:
        sum_of_humidity += humidity

    for i in range(1, 6, 2):
        print(i, sum_of_humidity / len(workroom_humidity))
