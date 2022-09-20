class Slurmik:

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_value):
        if not isinstance(new_value, str) or len(new_value) <= 0:
            raise ValueError("Имя должно быть непустой строкой")
        self.__name = new_value

    def __init__(self, name: str, profession: str, experience: int):
        """
        Конструктор
        :param name: Имя слёрмика
        :param profession: профессия слёрмика
        :param experience: стаж слёрмика
        """
        self.__name = name
        self.__profession = profession
        self.__experience = experience

    def say_hello(self):
        """
        Приветствует программиста
        :return:
        """
        print(f"Привет! Я слёрмик {self.__name}. Я {self.__profession}, мой стаж {self.__experience} лет.")


class SlurmikDev(Slurmik):

    def __init__(self, name: str, profession: str, experience: int, favorite_lang: str):
        """
        Конструктор
        :param name: Имя слёрмика
        :param profession: профессия слёрмика
        :param experience: стаж слёрмика
        """
        super().__init__(name, profession, experience)
        self.__name = name
        self.__profession = profession
        self.__experience = experience
        self.__fav_lang = favorite_lang

    def write_program(self, code_row_count):
        print(f"Я {self.name} и я пишу программу из {code_row_count} строк кода на {self.__fav_lang}")

        # self.__name = self.name
        # print(f"Я {self.__name} и я пишу программу из {code_row_count} строк кода на {self.__fav_lang}")
        # так тоже можно


def main():
    slurmik_vanya = Slurmik("Иван", "DevOps engineer", 14)
    slurmik_masha = Slurmik("Маша", "DevOps engineer", 10)
    slurmik_dima = SlurmikDev("Влад", "Программист", 6, "Ruby")

    slurmik_vanya.say_hello()
    slurmik_masha.say_hello()
    slurmik_dima.say_hello()

    slurmik_dima.name = "Дима"

    slurmik_dima.say_hello()
    slurmik_dima.write_program(200)


if __name__ == '__main__':
    main()
