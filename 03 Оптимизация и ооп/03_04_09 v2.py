EXPERIENCE = 6

def log_function_using(functor):
    
    def decorate(*args):
        print("функция была вызвана")
        result = functor(*args)
        print(f"функция была завершена, будет выведено значение {result}")
        return result
    return decorate

@log_function_using
def increase_experience(old_value):
    return old_value + 1


def main():
    exp = 6
    exp = increase_experience(exp)
    print(exp)

if __name__ == '__main__':
    main()