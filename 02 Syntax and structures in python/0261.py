if __name__ == '__main__':
    vendor = input('фирма холодильника')
    fridge_height = int(input('высота'))
    fridge_width = int(input('ширина'))

    is_pass_through_door = fridge_height <= 210 and fridge_width <= 90
    is_pass_throught_window = fridge_height <= 170 and fridge_width <= 320

    if vendor.lower() in ("brrr", "smf") and (is_pass_through_door or is_pass_throught_window):
        print('fits')
    else:
        print('не подходит')
