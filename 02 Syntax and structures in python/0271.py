from curses.ascii import isdigit
from tkinter.messagebox import NO


if __name__ == '__main__':
    last_humidity = None
    while last_humidity is None:
        print('input humidity (целое число)')
        input_data = input()
        if input_data.isdigit():
            last_humidity = int(input_data)
    workroom_hum = (32, 44, 44, 45, 46, 47, 60, 30, last_humidity)

    sum_of_humidity = 0
    for humidity in workroom_hum:
        sum_of_humidity += humidity
    
    for i in range(1, 6):
        print(i, sum_of_humidity/len(workroom_hum))
