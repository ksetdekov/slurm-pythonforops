class MetricCollector():
    def __init__(self, settings_dict) -> None:
        # Агент должен иметь IP адрес сервера, к которому подключается, 
        # хранить ключ доступа к серверу и 
        # иметь возможность управлять периодом сбора метрик(в секундах) 
        # и периодом отправки событий на сервер сбора событий (в секундах).
        self.ip_address = settings_dict['ip_address']
        self.server_key = settings_dict['server_key']
        self.collection_frequency = settings_dict['collection_frequency']
        self.send_frequency = settings_dict['collection_frequency']
        self.collect_counter = 0
    
    def __str__(self) -> str:
        list_of_attributes = [self.ip_address, self.server_key, self.collection_frequency, self.send_frequency, self.collect_counter]
        list_of_strings = [str(value) for value in list_of_attributes]
        return ", ".join(list_of_strings)

    def get_events(self):
    # Собрать события: при его использовании должно выводиться сообщение "события сервера <IP-адрес> собраны. Следующий сбор через <период сбора метрик> секунд".
        self.collect_counter += 1
        print(f"события сервера {self.ip_address} собраны. Следующий сбор через {self.collection_frequency} секунд")

    def send_events(self):
    # Отправка событий на сервер сбора метрик: выводится сообщение "события сервера <IP-адрес> собраны, отправлены на сервер сбора метрик. Следующая отправка через <период отправки событий на сервер сбора событий> секунд".
        self.collect_counter += 1
        print(f"события сервера {self.ip_address} собраны, отправлены на сервер сбора метрик. Следующая отправка через {self.send_frequency} секунд")
    
    def clear_cache(self):
    # Обнуление кеша агента: выводится сообщение "кеш агента был очищен" и  число вызовов метода сборки событий сбрасывается на 0.
        self.collect_counter = 0
        print("кеш агента был очищен")

    def get_event_count(self):
    # Получение информации о числе собранных событий: выводится сообщение "С сервера <IP-адрес> собрано <число вызовов метода сборки событий> событий".
        print(f"С сервера {self.ip_address} собрано {self.collect_counter} событий")


def main():
    metric_server = MetricCollector(settings_dict={'ip_address':'1.1.1.1', 'server_key':'fjkdsflsdfjdslf', 'collection_frequency':17, 'send_frequency':11})
    print(metric_server)
    metric_server.get_events()
    metric_server.get_events()
    metric_server.get_events()
    metric_server.send_events()
    metric_server.get_event_count()
    print(metric_server)
    metric_server.clear_cache()
    metric_server.send_events()
    metric_server.get_event_count()
    print(metric_server)


if __name__ == '__main__':
    main()
