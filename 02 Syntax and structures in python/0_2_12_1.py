def get_email_and_job_from_input():
    """
    Получение почты и профессия сотрудника и из потока вывода
    :return: почты и профессия сотрудника
    """
    print("Введите email")
    email = input()
    if email == "":
        print("Ввод прерван")
        return None, None
    print("Введите профессию")
    job = input()
    return email, job

def get_access_details_from_input():
    """
    Получение даты открытия доступа и периода доступа из потока ввода
    :return: даты открытия доступа и период доступа
    """
    print("Введите дату открытия доступа")
    access_from = input()
    print("Введите период доступа (в днях)")
    try:
        access_period = input()
        access_period = int(access_from)
    except ValueError:
        return None, None
    finally:
        print(f"Дата открытия доступа {access_from}, период доступа {access_period}")

    return access_from, access_period

def get_system_info(job):
    """
    Получение информаци о системе в которую предоставляем права
    :param job: профессия
    :return:
    """
    if job == "Программист":
        return "CKB", 1
    elif job == "Дизайнер":
        return "Иллюстратор", 3
    else:
        print("АХО через три двери направо")
        return None, None

def allow_access_to_user(email, system, access_details):
    """
    Выдача права в систему
    :param email: Почта сотрудника
    :param system: Название системы
    :param access_attempts: Количество попыток для выдачи прав
    :return:
    """
    for _ in range(access_details[0]):
        print(f"{email} был выдан доступ в {system}")

def main():
    processed_employees = 0
    while processed_employees < 5:

        email, job = get_email_and_job_from_input()
        if email is None and job is None:
            break

        access_from, access_period = get_access_details_from_input()

        system, access_attempts = get_system_info(job)

        if system is None and access_attempts is None:
            allow_access_to_user(email, access_details=(1, access_from, access_period), system="sanitary_engineering_room")
            continue

        allow_access_to_user(email, access_details=(access_attempts, access_from, access_period), system=system)

        processed_employees += 1
        print(f"Было внесено {processed_employees} сотрудников, осталось {5 - processed_employees}")

if __name__ == '__main__':
    main()