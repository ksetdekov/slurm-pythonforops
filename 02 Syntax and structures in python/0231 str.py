if __name__ == '__main__':
    name = 'kirill'
    job = 'data scientist'
    email = 'ksetdekov@gmail.com'

    who_am_i = f"Меня зовут {name:>30}, я {job}, пишите мне на {email}"
    print(who_am_i)

    # 2.3.8
    pod_name = "Pod"
    replicaset_name = "Replicaset"
    kubernetes_structures_desc = "Для объединения нескольких контейнеров в одну минимальную логическую единицу используется, в то время как контролирует количество реплик приложения"
    print(f"Для объединения нескольких контейнеров в одну минимальную логическую единицу используется {pod_name}, в то время как {replicaset_name} контролирует количество реплик приложения")
