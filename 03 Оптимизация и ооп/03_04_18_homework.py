# Доработайте класс для агента сбора метрик. Внедрите концепции инкапсуляции.

# Агент должен иметь возможность изменять период сбора метрик и период отправки событий на сервер 
# сбора событий. Внутри все периоды должны храниться в секундах. Но при реконфигурации должна быть 
# возможность задать период в формате "<Число>h<Число>m<Число>s",
#  это описание необходимо перевести в секунды.

# <Число>h - Число часов для установки периода
# <Число>m - Число минут для установки периода
# <Число>s - Число секунд для установки периода
# Порядок следования гарантировано не будет нарушен и других вариаций быть не может. 
# Но какие-то части выражения могут отсутствовать. Например будут валидными значения:

# 1h32m14s
# 32m14s
# 1h14s
# 14s
# Также не налагается запрет на ввод нарушающих атомарность временных значений. 
# То есть запись 134m91s должна считаться валидной и должна быть правильно преобразована.

# На отрицательные значения налагаются ограничения - 
# в случае их указания программа должна бросать исключение ValueError.

# Теперь давайте создадим специализации классов агента сбора метрик для Prometheus и Carbon.
#
# Агент для Prometheus не имеет дополнений к родительским полям. Но не позволяет управлять периодом отправки событий,
# т.к. работает в модели pull.
import re


class MetricCollector:
    def __init__(self, ip_address, server_key, collection_frequency, send_frequency) -> None:
        # Агент должен иметь IP адрес сервера, к которому подключается, 
        # хранить ключ доступа к серверу и 
        # иметь возможность управлять периодом сбора метрик(в секундах) 
        # и периодом отправки событий на сервер сбора событий (в секундах).
        self.ip_address = ip_address
        self.server_key = server_key
        self.__collection_frequency = collection_frequency
        self.__send_frequency = send_frequency
        self.collect_counter = 0

    def __str__(self) -> str:
        list_of_attributes = [self.ip_address, self.server_key, self.__collection_frequency, self.__send_frequency,
                              self.collect_counter]
        list_of_strings = [str(value) for value in list_of_attributes]
        return ", ".join(list_of_strings)

    @staticmethod
    def process_times(timestring):
        if isinstance(timestring, (int, float)):
            if timestring >= 0:
                return timestring
            else:
                raise ValueError('Введено отрицательное время')
        elif len(timestring) == 0:
            raise ValueError('Время не введено')
        else:
            time_seconds = MetricCollector.convert_string_to_seconds(timestring)
            return time_seconds

    @staticmethod
    def convert_string_to_seconds(timestring):
        time_seconds = 0
        time_seconds = MetricCollector.get_time_component_from_str(timestring, time_seconds, 'h')
        time_seconds = MetricCollector.get_time_component_from_str(timestring, time_seconds, 'm')
        time_seconds = MetricCollector.get_time_component_from_str(timestring, time_seconds, 's')
        return time_seconds

    @staticmethod
    def get_time_component_from_str(timestring, time_seconds, time_component):
        time_multipliers = {'h': 3600, 'm': 60}
        h_match = re.search(rf"[-\d]*?(?={time_component})", timestring)
        if h_match is not None:
            value_found = int(h_match[0])
            if value_found < 0:
                raise ValueError(f'Введено время как строка с отрицательным значением {time_component}')
            time_seconds += int(h_match[0]) * time_multipliers.get(time_component, 1)
        return time_seconds

    @property
    def collection_frequency(self):
        return self.__collection_frequency

    @collection_frequency.setter
    def collection_frequency(self, new_value):
        self.__collection_frequency = self.process_times(new_value)

    @property
    def send_frequency(self):
        return self.__send_frequency

    @send_frequency.setter
    def send_frequency(self, new_value):
        self.__send_frequency = self.process_times(new_value)

    def get_events(self):
        # Собрать события: при его использовании должно выводиться сообщение
        # "события сервера <IP-адрес> собраны. Следующий сбор через <период сбора метрик> секунд".
        self.collect_counter += 1
        print(f"события сервера {self.ip_address} собраны. Следующий сбор через {self.__collection_frequency} секунд")

    def send_events(self):
        # Отправка событий на сервер сбора метрик: выводится сообщение "события сервера <IP-адрес> собраны, отправлены
        # на сервер сбора метрик. Следующая отправка через <период отправки событий на сервер сбора событий> секунд".
        print(f"события сервера {self.ip_address} собраны, "
              f"отправлены на сервер сбора метрик. Следующая отправка через {self.__send_frequency} секунд")

    def clear_cache(self):
        # Обнуление кеша агента: выводится сообщение "кеш агента был очищен"
        # и число вызовов метода сборки событий сбрасывается на 0.
        self.collect_counter = 0
        print("кеш агента был очищен")

    def get_event_count(self):
        # Получение информации о числе собранных событий: выводится сообщение
        # "С сервера <IP-адрес> собрано <число вызовов метода сборки событий> событий".
        print(f"С сервера {self.ip_address} собрано {self.collect_counter} событий")


class PrometheusAgent(MetricCollector):
    # Агент для Prometheus не имеет дополнений к родительским полям. 
    # Но не позволяет управлять периодом отправки событий т.к. работает в модели pull.
    def send_events(self):
        self.collect_counter += 1
        print(f"события сервера {self.ip_address} собраны, отправлены по запросу от Prometheus")

    @MetricCollector.collection_frequency.setter
    def collection_frequency(self, new_value):
        print(f'Попытка поменять collection frequency с {self.collection_frequency} на {new_value}. Нельзя '
              f'устанавливать collection_frequency в этом агенте')


class CarbonAgent(MetricCollector):
    # Агент для Carbon в дополнение к родительским полям позволяет указать адрес сервера Carbon.
    def __init__(self, ip_address, server_key, collection_frequency, send_frequency, carbon_server=None) -> None:
        super().__init__(ip_address, server_key, collection_frequency, send_frequency)
        self.carbon_server = carbon_server

    def send_events(self):
        self.collect_counter += 1
        print(f"события сервера {self.ip_address} собраны, отправлены в Carbon. "
              f"Следующая отправка через {self.send_frequency} секунд")


def main():
    base_settings = {'ip_address': '1.1.1.1', 'server_key': 'fjkdsflsdfjdslf', 'collection_frequency': 17,
                     'send_frequency': 11}
    metric_server = MetricCollector(**base_settings)
    print(metric_server)
    metric_server.get_events()
    metric_server.get_events()
    metric_server.get_events()
    metric_server.send_events()
    metric_server.get_event_count()
    metric_server.collection_frequency = '1h1m1s'
    metric_server.send_frequency = '1h22m1s'

    print(metric_server)
    metric_server.clear_cache()
    metric_server.send_events()
    metric_server.get_event_count()
    print(metric_server)

    print("проверка что у всех экземпляров разных классов работает метод send_events")

    regular_collector = MetricCollector(**base_settings)
    prometheus_collector = PrometheusAgent(**base_settings)
    carbon_collector = CarbonAgent(carbon_server='198.168.1.1', **base_settings)

    for agent in [regular_collector, carbon_collector, prometheus_collector]:
        agent.send_events()

    print("проверка что у агента для Carbon есть новое свойство")
    print(carbon_collector.carbon_server)

    print(prometheus_collector)
    prometheus_collector.collection_frequency = '1m'
    print(prometheus_collector)
    prometheus_collector.send_frequency = '4h20s'
    print(prometheus_collector)


if __name__ == '__main__':
    main()
