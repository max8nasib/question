def is_prime(n):
    # Простые числа начинаются с 2
    if n < 2:
        return False
    # Проверяем делители до квадратного корня из n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


# Основной цикл программы
while True:
    try:
        start = int(input("Введите начальное число диапазона: "))
        end = int(input("Введите конечное число диапазона: "))

        # Проверяем корректность диапазона
        if start > end:
            raise ValueError("Начальное число не может быть больше конечного!")

        # Получаем и выводим простые числа
        result = get_primes(start, end)
        print(f"Простые числа в диапазоне [{start}, {end}]: {result}")
        break
    except ValueError:
        print(f"Пожалуйста, введите корректные числа!")
