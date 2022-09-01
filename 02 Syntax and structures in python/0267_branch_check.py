if __name__ == '__main__':
    # get inputs
    branch_name = input('branch name:')
    is_test_passed = int(input('test pass results (1 for true, 0 for false):'))
    change_in_coverage = float(input('change in coverage:'))
    number_approves = int(input('how many approves?:'))

    # 2 testes for release:
    # Если все тесты прошли и coverage вырос более чем на 5 процентов,
    # то такую ветку нужно отправлять в релиз, даже если нужное количество approve не набралось.
    first_test = is_test_passed == 1 and change_in_coverage > 0.05
    # Если все тесты прошли и coverage вырос ровно или менее чем на 5 процентов,
    # набралось более 3 approve - код так же можно отправлять в релиз.
    second_test = is_test_passed == 1 and change_in_coverage <= 0.05 and number_approves > 3

    if branch_name.lower() not in ('development', 'staging'):
        print(f"В ветке {branch_name} непроверенный код, пропускаем")
    elif first_test or second_test:
        print(f"Внимание! Код из {branch_name} отправлен в релиз!")
    else:
        # готовим строку про тесты
        pass_results_options = ("не пройдены", "пройдены")
        pass_results_string = pass_results_options[is_test_passed]
        print(f"Код из {branch_name} с результатами тесты: {pass_results_string}, coverage: {change_in_coverage}, approve: {number_approves} в релиз не попадает.")
