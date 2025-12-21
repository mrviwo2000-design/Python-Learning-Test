class MathCalculator:
    """
    Класс для выполнения математических операций
    """

    def add(self, a: float, b: float) -> float:
        """
        Сложение двух чисел
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        Вычитание двух чисел
        """
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """
        Умножение двух чисел
        """
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        Деление двух чисел
        """
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b

    def power(self, base: float, exponent: float) -> float:
        """
        Возведение в степень
        """
        if base == 0 and exponent < 0:
            raise ValueError("Ноль в отрицательной степени не определен")
        return base ** exponent

    def factorial1(self, n: int, s: Str) -> int:
        """
        Вычисление факториала числа
        """
        if n < 0:
                raise ValueError("Факториал отрицательного числа не определен")
            
        if Str == "Рек":
                result = 1
            if n <= 1:  # базовый случай
                return 1
            return n * factorial2(n - 1)  # рекурсивный случай
        
        elif Str == "Не рек":
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result

    def is_prime(self, n: int) -> bool:
        """
        Проверка числа на простоту
        """
        if n < 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def fibonacci(self, n: int) -> int:
        """
        Вычисление n-го числа Фибоначчи
        """
        if n < 0:
            raise ValueError("Число Фибоначчи для отрицательного индекса не определено")
        if n == 0:
            return 0
        elif n == 1:
            return 1

        a, b = 0, 1
        print(0)
        for _ in range(2, n + 1):
            print(b)
            a, b = b, a + b
        return b
    def procent(self, n: int) -> int:
        """
        Деление числа на 100 -> процентное число
        """
        if n < 0:
            return False
        if n >= 0:
            n = n / 100
            return n

def main():
    """
    Основная функция приложения
    """
    calculator = MathCalculator()

    print("Математический калькулятор")
    print("Доступные операции:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Факториал (Рек; Не рек)")
    print("7. Проверка на простое число")
    print("8. Число Фибоначчи")
    print("9. Число в процент")

    try:
        choice = input("Выберите операцию (1-9): ")

        if choice in ['1', '2', '3', '4', '5']:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))

            if choice == '1':
                result = calculator.add(a, b)
                print(f"Результат: {a} + {b} = {result}")
            elif choice == '2':
                result = calculator.subtract(a, b)
                print(f"Результат: {a} - {b} = {result}")
            elif choice == '3':
                result = calculator.multiply(a, b)
                print(f"Результат: {a} * {b} = {result}")
            elif choice == '4':
                result = calculator.divide(a, b)
                print(f"Результат: {a} / {b} = {result}")
            elif choice == '5':
                result = calculator.power(a, b)
                print(f"Результат: {a} ^ {b} = {result}")

        elif choice in ['6', '7', '8', '9']:
            n = int(input("Введите число: "))

            if choice == '6':
                result = calculator.factorial(n)
                print(f"Факториал {n} = {result}")
            elif choice == '7':
                result = calculator.is_prime(n)
                status = "простое" if result else "не простое"
                print(f"Число {n} - {status}")
            elif choice == '8':
                result = calculator.fibonacci(n)
                print(f"Число Фибоначчи F({n}) = {result}")
            elif choice == '9':
                result = calculator.procent(n)
                print(f"Число в процентах {n} / 100 = {result}")

        else:
            print("Неверный выбор операции")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":

    main()


