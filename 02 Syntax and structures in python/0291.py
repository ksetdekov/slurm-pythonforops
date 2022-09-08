from msilib import MSIMODIFY_VALIDATE
from tkinter.messagebox import NO


if __name__ == '__main__':
    info_about_me = {"name": "kirill", "temp": 24, "hum": 60}
    print(info_about_me["name"])

    info_about_me["is_i_love_python"] = True
    print(info_about_me)

    info_about_me["hum"] = 50
    print(info_about_me)

    temp_1 = info_about_me.get("temper")
    if temp_1 is None:
        print("no info about temper")
    
    print(list(info_about_me.items()))

    info_about_me.update({'temp':10, 'cat_count':0})
    print(info_about_me)

    pair = info_about_me.popitem()
    print(pair)
    print(info_about_me)

    value = info_about_me.pop("hum")
    print(f"humidity is {value}")
    print(info_about_me)

    # mutable type
    info_about_me_2 = info_about_me.copy()
    info_about_me_2["cat_count"] = 0
    print(info_about_me)

    # setdefault
    value = info_about_me.setdefault("surname", "setdekov")
    print(value)
    print(info_about_me)

    # from keys
    my_dict = dict.fromkeys(["first", "second", 3], "hello from keys")
    print(my_dict)

    mylist = ['first', 'second',  3]
    my_values = [1, 2, 3]
    print(list(zip(mylist, my_values)))