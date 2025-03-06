""" Программа декодируюшая команды. """


def check_brackets(command):
    """
    Проверяет баланс скобок в строке
    """
    count = 0
    for char in command:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0


def decode(command):
    """
    Декодирует команду с учетом вложенных скобок
    """
    # Удаляем внешние скобки
    command = command[1:-1]

    # Ищем число перед скобками
    num = ''
    i = 0
    while i < len(command) and command[i].isdigit():
        num += command[i]
        i += 1

    # Если нет числа, считаем как 1
    num = int(num) if num else 1

    # Если есть вложенные скобки
    if '(' in command[i:]:
        result = ''
        while i < len(command):
            if command[i] == '(':
                # Находим соответствующую закрывающую скобку
                start = i
                count = 1
                for j in range(i + 1, len(command)):
                    if command[j] == '(':
                        count += 1
                    elif command[j] == ')':
                        count -= 1
                        if count == 0:
                            end = j
                            break
                # Декодируем содержимое вложенных скобок
                result += decode(command[start:end + 1])
                i = end
            else:
                result += command[i]
            i += 1
    else:
        result = command[i:]

    return result * num


def main():
    while True:
        command = input("Введите команду для дешифровки: ")

        # Проверяем корректность ввода
        if not check_brackets(command):
            print("Ошибка: некорректное количество скобок!")
            continue

        if not (command.startswith('(') and command.endswith(')')):
            print("Ошибка: команда должна быть заключена в скобки!")
            continue

        try:
            result = decode(command)
            print(f"Результат дешифровки: {result}")
            break
        except:
            print("Ошибка: некорректная команда!")


if __name__ == "__main__":
    main()