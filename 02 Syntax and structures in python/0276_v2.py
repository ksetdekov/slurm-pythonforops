if __name__ == '__main__':
    processed_employees = 0
    while processed_employees < 5:
        email = input("enter email:")
        job = input("enter prof:")
        if email == "":
            print('ввод прерван')
            break

        system = None
        access_attempts = None

        if job == "Программист":
            system = "CKB"
            access_attempts = 1
        elif job == "Дизайнер":
            system = "Иллюстратор"
            access_attempts = 3
        else:
            print("АХО через три двери направо")
            continue

        for _ in range(access_attempts):
            print(f"{email} был выдан доступ в {system}")

        processed_employees += 1
        print(
            f"Было внесено {processed_employees} сотрудников, осталось {5 - processed_employees}")
