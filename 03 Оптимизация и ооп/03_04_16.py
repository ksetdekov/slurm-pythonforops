class Slurmik:

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_value):
        if not isinstance(new_value, str) or len(new_value) <= 0:
            raise ValueError("Имя должно быть непустой строкой")
        self._name = new_value

    def __init__(self, name: str, profession: str, experience: int):
        """
        Конструктор
        :param name: Имя слёрмика
        :param profession: профессия слёрмика
        :param experience: стаж слёрмика
        """
        self._name = name
        self._profession = profession
        self._experience = experience

    def say_hello(self):
        """
        Приветствует программиста
        :return:
        """
        print(f"Привет! Я слёрмик {self._name}. Я {self._profession}, мой стаж {self._experience} лет.")


class SlurmikDev(Slurmik):

    def __init__(self, name: str, profession: str, experience: int, favorite_lang: str):
        """
        Конструктор
        :param name: Имя слёрмика
        :param profession: профессия слёрмика
        :param experience: стаж слёрмика
        """
        super().__init__(name, profession, experience)
        self.__fav_lang = favorite_lang

    def write_program(self, code_row_count):
        print(f"Я {self.name} и я пишу программу из {code_row_count} строк кода на {self.__fav_lang}")

    def say_hello(self):
        """
        Приветствует программиста
        :return:
        """
        print(f"Привет! Я слёрмик {self._name}. "
              f"Я {self._profession}, "
              f"мой стаж программирования {self._experience} лет.")


def main():
    slurmik_vanya = Slurmik("Иван", "DevOps engineer", 14)
    slurmik_masha = Slurmik("Маша", "DevOps engineer", 10)
    slurmik_dima = SlurmikDev("Влад", "Программист", 6, "Ruby")

    for slurmik in [slurmik_vanya, slurmik_masha, slurmik_dima]:
        slurmik.say_hello()


if __name__ == '__main__':
    main()
