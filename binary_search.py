""" Программа мини-игра на принципе бинарного поиска """


# Запрос чисел от пользователя.
def binary_search():
    print("Привет, давай сыграем в игру на принципе бинарного поиска? "
          "Введите диапазон для загадываемого числа.")
    while True:
        try:
            low = int(input("Введите первое число: "))
            high = int(input("Введите второе число: "))
            # Проверка цисел
            if low >= high:
                print("Первое число должно быть меньше второго. "
                      "Попробуйте снова.")
                continue
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите числа.")

    # Основной цикл программы.
    print("Загадайте число в заданном диапазоне, "
          "если хотите выйти введите 'выход'. ")
    while low <= high:
        mid = (low + high) // 2
        response = (input(f"Ваше число больше {mid}? (да/нет): ")
                    .strip().lower())

        if response == 'да':
            low = mid + 1
        elif response == 'нет':
            high = mid - 1
        elif response == 'выход':
            exit("до встречи!")
        else:
            print("Некорректный ввод. Ответьте 'да' или 'нет' или 'выход'.")

    print(f"Вы загадали число {low}!")


# Вывод всей программы.
binary_search()
