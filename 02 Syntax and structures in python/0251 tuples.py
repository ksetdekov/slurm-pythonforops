if __name__ == '__main__':
    trash_can = ('denis', True, 0)

    name, is_i_love_python, cat_count = trash_can
    print(name, is_i_love_python, cat_count)
    climate = (21, 53)
    print(trash_can + climate)

    cat_count, temp, humid = (trash_can + climate)[2:]
    print(cat_count, temp, humid)

    name = 'bob'
    a, b, c = name
    print(a, b, c)

    basic_courses = ("Docker", "Ansible", "Ceph")
    advanced_courses = ("Kubernetes База", "Kubernetes Мега")

    print((basic_courses + advanced_courses)[1::3])