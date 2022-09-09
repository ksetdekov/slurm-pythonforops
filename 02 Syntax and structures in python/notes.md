# Основы синтаксиса и структуры в Python

* синтаксис и среда разработки
* требования к codestyle
* структуру программы в процедурной парадигме
* облегчающие жизнь встроенными методами типов данных
* ошибаемся и обрабатываем ошибки и отладка

## числа в python

* бывают целые и вещественные и комплексные, атомарный тип данных в python
* числа - immutable

## strings

синтаксис форматирования в строках <https://docs.python.org/3.9/library/string.html#formatstrings>

* lstrip/rstrip/strip
  * можно передать много символов

    ```python
    str().strip("_ ?!")
    ```

* upper, lower, capitalize
* replace

```python
str().replace("что заменить", "на что заменить", 1)
# 3й агрумент - сколько раз начиная слева заменяет
```

### индексация

все элементы строки нумерованы с 0 и справа налево с -

### срезы - выбор с индекса по индекс

начиная с элемента начала до конца, не включая конец

```python
print('0123456'[2:5])
# 234
```

срез с шагом [A:B:step] с A по B с шагом step, не включая B

```python
print('0123456'[:6:3])
# 03
```

## logical types

операторы: или, и

## tuples

неизменяемый тип данных, очень похож на строки

## data types

* immutable - int, float, bool, str, tuples
* mutable - list, dict, set

## условные операторы

```python
if xxx > y:
  print('do')
else:
  print('else')
```

## Cycles

* while - выполнять пока условие не станет нужным
* for - пока в итерируемом объекте есть значения

### прерывание циклов

* break
* continue

## lists

* append
* extend - расширяет текущий список
* pop - удалил последний элемент из списка
* reverse
* sort
* clear - очистить список
* copy - скопировать исходный список

## dicts

просто словари - ничего нового
состовный изменяемый тип данных

## sets множества

полезная инфа <https://habr.com/ru/post/516858/>
состовный изменяемый тип данных

 ```python
 set()
 ```

уникальные значения

* remove - удалить и кинуть ошибку если нет
* discard -  безопасно удалить
* удалить элемент и получить удаленный
* issubset (что все входят в другое)
* issuperset (обратное к issubset)
* copy - скопировать все значения
* intersect - пересечь
* difference - вычесть из первого множество - множество аргумента
* symmetrical_difference - только элементы, которые  есть только в одном
* union - объединение

Лучше их брать для учета уникальности, если надо считать разницу и дискретной математикой говорить. Иначе - лучше брать список.

## Функции

абстракции

1. Выражения
2. Фукнкции
3. Модуль
4. Микросервисы
5. Подсистемы

Зачем нужно?

1. Не дубливровать код.
2. Централизованно им управлять
3. Создавать свои модули.

### принцип единственной ответственности

* функция делает что-то одно
* передавать не больше 5 аргументов за раз
* наименовать как глагол

если работаем со списками как аргументы в функциях, чтобы не начать менять их - лучше делать такую конструкцию

```python
def work_with_mutables(my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(3)
    print(my_list)

def main():
    for _ in range(6):
        work_with_mutables()

if __name__ == '__main__':
    main()
```

```bash
[3]
[3]
[3]
[3]
[3]
[3]

Process finished with exit code 0
```

а вот так делать не нужно

```python
def work_with_mutables(my_list=[]):
    my_list.append(3)
    print(my_list)

def main():
    for _ in range(6):
        work_with_mutables()

if __name__ == '__main__':
    main()
```

```bash
[3]
[3, 3]
[3, 3, 3]
[3, 3, 3, 3]
[3, 3, 3, 3, 3]
[3, 3, 3, 3, 3, 3]

Process finished with exit code 0
```

## global and local vars

1. local
2. enclosed - nonlocal variable
3. global
4. built-in

```python
variable = "global"

def main():
    global variable
    variable = "enclosed"

    def sub_main():
        # nonlocal variable
        # variable = "local"
        print(variable)

    sub_main()
    print(variable)

if __name__ == '__main__':
    main()
    print(variable)
```

## try except

* try
* except
* finally

PDB debugger

```bash
python3 -m pdb main.py
```

можно ходить по программе через step
list можно говорить про строку

break \< num \>  

можно писать help
