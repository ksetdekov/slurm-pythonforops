if __name__ == "__main__":
    name = '   ---денис--   '
    job = 'R&D рAзРаБоТчИк'
    email = 'ksetdekov@gmail.com'
    secret_symbol_second_part = "w5g3t3g2j"
    secret_symbol_first_part = "wer4605rtrt"
    secret_symbol = chr(int(secret_symbol_first_part[3:7]) + int(secret_symbol_second_part[1::2]))
    result = f"Меня зовут {name.strip(' -').capitalize()}, я {job.lower()}, пишите мне на {email.replace('@' , ' at ')}{secret_symbol}"
    print(result)