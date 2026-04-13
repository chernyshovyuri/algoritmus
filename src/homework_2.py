import csv




def factorial(n: int) -> int | None:
    if not isinstance(n, int):
        raise TypeError()

    if n < 0 or n > 20:
        return None

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

def fibonaci(n: int | float)-> list[int|float] | None:
    if not isinstance(n, (int, float)):
        raise TypeError()

    if n <= 0:
        return None
    if n == 1:
        return [0]

    fib_list = [0, 1]

    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])

    return fib_list

def count_ones(n: int) -> int| None:
    if not isinstance(n, int):
        raise TypeError()

    if n < 0:
        return None

    if n == 0:
        return 0

    count =0
    while n > 0:
        if n % 2 == 1:
            count += 1
        n //= 2

    return count


def palindrome(n: int) -> bool | None:
    if not isinstance(n, int):
        raise TypeError()

    if n < 0:
        return None

    start_number = n
    finish_number = 0
    while n > 0:
        digit = n % 10
        finish_number = finish_number * 10 + digit
        n //= 10

    if start_number == finish_number:
        return True

    return False

# Проблема:
# Нужна программа котора будет обрабатывать посещаемость сайта. Необходимо пердоставить информацию о мах коичестве
# посещаемости и минимальном кол. посещаемости в разрезе дней. Необходимо сделать срез по 3 дням, 3 дня с самым
# мах посещением и з дня с минимальным посещением.

# выходные данные:
# Электронные таблицы где указано дата и количество посещений на эту дату. Четкая и понятная статистика.

# Входные данные:
#  Список дат с указанием посещений сайта

# Ограничения:
# Память 52 мб Скорость 5ск.

# Тестирование.
# Позитивные, негативные, пограничные.



def reading_file(path: str, date_tuples: list) ->list:
    if not isinstance(date_tuples, list):
        raise TypeError()


    with open(path, 'r') as file:
        for line in file:
            data_list = line.strip()
            if data_list:
                date, count = data_list.split(',')
                date_tuples.append((date, int(count)))

    return date_tuples


def record_table(result: tuple)-> None:

    if not result:
        return None

    max1, max2, max3, min1, min2, min3 = result

    with open('resources/date_visitors.csv', 'w', newline='', encoding='utf-8') as file:
        file.write(f'Рейтинг, Дата, Посещаемость\n')
        file.write(f'Максимум-1,{max1[0]},{max1[1]}\n')
        file.write(f'Максимум-2,{max2[0]},{max2[1]}\n')
        file.write(f'Максимум-3,{max3[0]},{max3[1]}\n')
        file.write(f'Минимум-1,{min1[0]},{min1[1]}\n')
        file.write(f'Минимум-2,{min2[0]},{min2[1]}\n')
        file.write(f'Минимум-3,{min3[0]},{min3[1]}\n')



def search_for_max_and_min_values(date:list | tuple)-> tuple| None:
    if not isinstance(date, (list, tuple)):
        raise TypeError()

    if not date:
        return None
    if len(date) < 3:
        return None

    max_value = max_value_2 = max_value_3 =date[0]

    min_value = min_value_2 = min_value_3 = date[0]


    for i in range(1, len(date)):
        variable = date[i][1]

        if variable > max_value[1]:
            max_value_3 = max_value_2
            max_value_2 = max_value
            max_value = date[i]
        elif variable > max_value_2[1]:
            max_value_3 = max_value_2
            max_value_2 = date[i]
        elif variable > max_value_3[1]:
            max_value_3 = date[i]


        if variable < min_value[1]:
            min_value_3 = min_value_2
            min_value_2 = min_value
            min_value = date[i]
        elif variable < min_value_2[1]:
            min_value_3 = min_value_2
            min_value_2 = date[i]
        elif variable < min_value_3[1]:
            min_value_3 = date[i]

    return (max_value, max_value_2, max_value_3, min_value, min_value_2, min_value_3)
































