def get_email_and_job_from_input():
    """
    Получение почти и работы из потока входа

    :return: почта и профессия сотрудника
    :rtype: (str, str)
    """
    email = input("enter email:")
    if email == "":
        print('ввод прерван')
        return None, None
    job = input("enter prof:")
    return email, job


def get_system_info(job):
    """
    выдает какие системы и сколько попыток по работе

    :param job: работа
    :type job: str
    :return: система и сколько попыток
    :rtype: (str, int)
    """
    if job == "Программист":
        return "CKB",  1
    elif job == "Дизайнер":
        return "Иллюстратор", 3
    else:
        print("АХО через три двери направо")
        return None, None


def grant_access_to_user(email, system, access_attempts):
    """выдача прав в систему

    :param email: почта
    :type email: str
    :param system: система
    :type system: str
    :param access_attempts: сколько попыток делать
    :type access_attempts: int
    """
    for _ in range(access_attempts):
        print(f"{email} был выдан доступ в {system}")


def main():
    processed_employees = 0
    while processed_employees < 5:
        email, job = get_email_and_job_from_input()

        if email is None and job is None:
            print('ввод прерван')
            break

        system, access_attempts = get_system_info(job)
        if system is None and access_attempts is None:
            grant_access_to_user(email, access_attempts=1, system="sanitary_engineering_room")
            continue

        grant_access_to_user(email, system, access_attempts)

        processed_employees += 1
        print(
            f"Было внесено {processed_employees} сотрудников, осталось {5 - processed_employees}")


if __name__ == '__main__':
    main()
