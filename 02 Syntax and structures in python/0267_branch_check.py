if __name__ == '__main__':
    # get inputs
    branch_name = input('branch name:')
    is_test_passed = bool(
        int(input('test pass results (1 for true, 0 for false):')))
    change_in_coverage = float(input('change in coverage:'))
    number_approves = int(input('how many approves?:'))

    if branch_name.lower() not in ('development', 'staging'):
        print(f"В ветке {branch_name} непроверенный код, пропускаем")
    # проверки на release в 1 строку
    # Если все тесты прошли и coverage вырос более чем на 5 процентов,
    # то такую ветку нужно отправлять в релиз, даже если нужное количество approve не набралось.
    # Если все тесты прошли и coverage вырос ровно или менее чем на 5 процентов,
    # набралось более 3 approve - код так же можно отправлять в релиз.
    elif is_test_passed and (change_in_coverage > 0.05 or (0 < change_in_coverage <= 0.05 and number_approves > 3)):
        print(f"Внимание! Код из {branch_name} отправлен в релиз!")
    else:
        # готовим строку про тесты
        pass_results_string = "пройдены" if is_test_passed else "не пройдены"
        print(f"Код из {branch_name} с результатами тесты: {pass_results_string}, coverage: {change_in_coverage}, approve: {number_approves} в релиз не попадает.")
