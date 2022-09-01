if __name__ == "__main__":
    name = '   ---денис--   '
    job = 'R&D рAзРаБоТчИк'
    email = 'ksetdekov@gmail.com'
    secret_symbol_second_part = "w5g3t3g2j"
    secret_symbol_first_part = "wer4605rtrt"
    secret_symbol = chr(int(secret_symbol_first_part[3:7]) + int(secret_symbol_second_part[1::2]))
    result = f"Меня зовут {name.strip(' -').capitalize()}, я {job.lower()}, пишите мне на {email.replace('@' , ' at ')}{secret_symbol}"
    print(result)
    #2.3.15
    instruction_name = "Disaster recovery plan"
    print(instruction_name[9:-5])
    print(instruction_name[9:])
    print(instruction_name[:8])

    my_name = "Хикматилло"
    print(ord(my_name[0]))  # 1061
    is_my_name_long = my_name > 8
    print(is_my_name_long)