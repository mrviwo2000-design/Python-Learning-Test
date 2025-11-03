import pytest
from script import MathCalculator


class TestMathCalculator:
    """Тестирующий класс для MathCalculator"""

    @pytest.fixture
    def calculator(self):
        """Фикстура для создания экземпляра калькулятора"""
        return MathCalculator()

    # Группа: basic_operations
    @pytest.mark.basic_operations
    def test_add(self, calculator):
        """Тест сложения"""
        assert calculator.add(2, 3) == 5
        assert calculator.add(-1, 1) == 0
        assert calculator.add(0, 0) == 0

    @pytest.mark.basic_operations
    def test_subtract(self, calculator):
        """Тест вычитания"""
        assert calculator.subtract(5, 3) == 2
        assert calculator.subtract(0, 5) == -5
        assert calculator.subtract(-1, -1) == 0

    @pytest.mark.basic_operations
    def test_multiply(self, calculator):
        """Тест умножения"""
        assert calculator.multiply(4, 3) == 12
        assert calculator.multiply(0, 5) == 0
        assert calculator.multiply(-2, 3) == -6

    @pytest.mark.basic_operations
    @pytest.mark.parametrize("a, b, expected", [
        (10, 2, 5),
        (1, 4, 0.25),
        (-6, 3, -2),
        (0, 5, 0),
    ])
    def test_divide_parametrized(self, calculator, a, b, expected):
        """Параметризованный тест деления"""
        assert calculator.divide(a, b) == expected

    # Группа: advanced_operations
    @pytest.mark.advanced_operations
    def test_power(self, calculator):
        """Тест возведения в степень"""
        assert calculator.power(2, 3) == 8
        assert calculator.power(5, 0) == 1
        assert calculator.power(4, 0.5) == 2

    @pytest.mark.advanced_operations
    @pytest.mark.parametrize("n, expected", [
        (0, 1),
        (1, 1),
        (5, 120),
        (7, 5040),
    ])
    def test_factorial_parametrized(self, calculator, n, expected):
        """Параметризованный тест факториала"""
        assert calculator.factorial(n) == expected

    # Группа: number_theory
    @pytest.mark.number_theory
    def test_is_prime(self, calculator):
        """Тест проверки простых чисел"""
        assert calculator.is_prime(2) == True
        assert calculator.is_prime(17) == True
        assert calculator.is_prime(4) == False
        assert calculator.is_prime(1) == False
        assert calculator.is_prime(0) == False

    @pytest.mark.number_theory
    def test_fibonacci(self, calculator):
        """Тест чисел Фибоначчи"""
        assert calculator.fibonacci(0) == 0
        assert calculator.fibonacci(1) == 1
        assert calculator.fibonacci(5) == 5
        assert calculator.fibonacci(10) == 55

    # Группа: exception_tests
    @pytest.mark.exception_tests
    def test_divide_by_zero(self, calculator):
        """Тест исключения при делении на ноль"""
        with pytest.raises(ValueError, match="Деление на ноль невозможно"):
            calculator.divide(5, 0)

    @pytest.mark.exception_tests
    def test_factorial_negative(self, calculator):
        """Тест исключения при факториале отрицательного числа"""
        with pytest.raises(ValueError, match="Факториал отрицательного числа не определен"):
            calculator.factorial(-5)

    @pytest.mark.exception_tests
    def test_power_zero_negative(self, calculator):
        """Тест исключения при возведении нуля в отрицательную степень"""
        with pytest.raises(ValueError, match="Ноль в отрицательной степени не определен"):
            calculator.power(0, -2)

    @pytest.mark.exception_tests
    def test_fibonacci_negative(self, calculator):
        """Тест исключения при отрицательном индексе Фибоначчи"""
        with pytest.raises(ValueError, match="Число Фибоначчи для отрицательного индекса не определено"):
            calculator.fibonacci(-1)

    # Группа: edge_cases
    @pytest.mark.edge_cases
    def test_edge_cases(self, calculator):
        """Тест граничных случаев"""
        # Большие числа
        assert calculator.add(1e10, 1e10) == 2e10

        # Дробные числа - используем приблизительное сравнение
        result = calculator.multiply(0.1, 0.1)
        expected = 0.01
        # Сравниваем с точностью до 10 знаков после запятой
        assert abs(result - expected) < 1e-10

        # Граница простых чисел
        assert calculator.is_prime(97) == True

    # Группа: float_precision
    @pytest.mark.float_precision
    @pytest.mark.parametrize("operation, a, b, expected", [
        ("add", 0.1, 0.2, 0.3),
        ("multiply", 0.1, 0.1, 0.01),
        ("multiply", 0.3, 0.3, 0.09),
        ("divide", 1.0, 3.0, 1.0 / 3.0),
    ])
    def test_float_operations_precision(self, calculator, operation, a, b, expected):
        """Параметризованный тест операций с плавающей точкой"""
        if operation == "add":
            result = calculator.add(a, b)
        elif operation == "multiply":
            result = calculator.multiply(a, b)
        elif operation == "divide":
            result = calculator.divide(a, b)

        # Используем приблизительное сравнение для чисел с плавающей точкой
        assert abs(result - expected) < 1e-10


# Дополнительные тесты для проверки типов
class TestMathCalculatorTypes:
    """Тесты для проверки типов данных"""

    @pytest.fixture
    def calculator(self):
        return MathCalculator()

    @pytest.mark.type_tests
    def test_float_operations(self, calculator):
        """Тест операций с дробными числами"""
        result = calculator.add(1.5, 2.5)
        assert result == 4.0
        assert isinstance(result, float)

    @pytest.mark.type_tests
    def test_int_operations(self, calculator):
        """Тест операций с целыми числами"""
        result = calculator.multiply(3, 4)
        assert result == 12
        assert isinstance(result, int)


# Тесты для проверки точности вычислений с использованием pytest.approx
class TestMathCalculatorPrecision:
    """Тесты для проверки точности вычислений с плавающей точкой"""

    @pytest.fixture
    def calculator(self):
        return MathCalculator()

    @pytest.mark.precision
    def test_float_addition_precision(self, calculator):
        """Тест точности сложения дробных чисел"""
        result = calculator.add(0.1, 0.2)
        expected = 0.3
        # Используем встроенную функцию pytest.approx для сравнения
        assert result == pytest.approx(expected)

    @pytest.mark.precision
    def test_float_multiplication_precision(self, calculator):
        """Тест точности умножения дробных чисел"""
        result = calculator.multiply(0.1, 0.1)
        expected = 0.01
        assert result == pytest.approx(expected)

    @pytest.mark.precision
    @pytest.mark.parametrize("a, b, expected", [
        (0.1, 0.2, 0.3),  # сложение
        (0.1, 0.1, 0.01),  # умножение
        (1.0, 3.0, 1.0 / 3.0),  # деление
    ])
    def test_float_operations_parametrized(self, calculator, a, b, expected):
        """Параметризованный тест точности операций с плавающей точкой"""
        if (a, b) == (0.1, 0.2):
            result = calculator.add(a, b)  # для 0.1 + 0.2 используем сложение
        else:
            result = calculator.multiply(a, b)  # для остальных случаев умножение

        assert result == pytest.approx(expected)


# Тесты для проверки граничных значений
class TestMathCalculatorBoundaries:
    """Тесты для проверки граничных значений"""

    @pytest.fixture
    def calculator(self):
        return MathCalculator()

    @pytest.mark.boundary
    def test_large_numbers(self, calculator):
        """Тест работы с большими числами"""
        large_num = 1e15
        assert calculator.add(large_num, large_num) == 2e15
        assert calculator.multiply(large_num, 2) == 2e15

    @pytest.mark.boundary
    def test_small_numbers(self, calculator):
        """Тест работы с очень маленькими числами"""
        small_num = 1e-15
        assert calculator.multiply(small_num, small_num) == pytest.approx(1e-30)

    @pytest.mark.boundary
    def test_zero_operations(self, calculator):
        """Тест операций с нулем"""
        assert calculator.add(0, 5) == 5
        assert calculator.multiply(0, 5) == 0
        assert calculator.power(5, 0) == 1