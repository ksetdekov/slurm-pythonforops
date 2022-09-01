if __name__ == '__main__':
    # Количество свободной оперативной памяти в облачном кластере в мегабайтах
    free_ram_amount = 200
    app_replicas = 2  # Количество реплик приложения
    # Есть ли возможность использовать дополнительную оперативную память при исчерпании лимита
    has_ram_overdraft = True
    balance = 10000  # Баланс лицевого счета в местной валюте

    has_replicas = app_replicas > 1
    mem_check = (free_ram_amount / app_replicas) >= 150
    price_mem_check =  has_ram_overdraft and (balance >= 8000)

    is_resistant = has_replicas and (mem_check or price_mem_check)

    print(is_resistant)