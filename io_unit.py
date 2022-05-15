import math


def handle_error(msg):
    print(msg)
    print("Enter = повторить ввод, любая другая клавиша + Enter = выход:")
    tmp = input()
    if tmp == "":
        return
    print("Программа завершает работу.")
    quit(-1)


def input_point():
    while 1:
        print("Введите начальное условие (действительные координаты X0 и Y0 через пробел, разделитель - точка):")
        try:
            tmp = input().split(" ")
            if len(tmp) != 2:
                raise ValueError()
            x = float(tmp[0])
            y = float(tmp[1])
            return x, y
        except ValueError:
            handle_error("Ошибка ввода! Требуется ввести два действительных числа через пробел (разделитель - точка).")


def choose_eq(x0, y0, eq=None, f=None, f_as_text=None):
    eq_list = ["y′ = (x-y)^2 + 1", "y′ = xy", "y′ = e^x + y", "y′ = x^2 - y"]
    print("Программа умеет работать со следующими уравнениями:")
    for i in range(len(eq_list)):
        print(str(i + 1) + ". " + eq_list[i])
    while 1:
        print("Введите номер нужного уравнения (целое число от 1 до 4):")
        try:
            tmp = int(input())
            if (tmp < 1) | (tmp > 4):
                raise ValueError()
            elif tmp == 1:
                c = x0 + 1 / (y0 - x0)
                f_as_text = "y = x + 1/(" + str(c) + " - x)"
                f = lambda x: x + 1 / (c - x)
                eq = lambda x, y: (x - y) ** 2 + 1
            elif tmp == 2:
                c = y0 / (math.e ** (x0 * x0 / 2))
                f_as_text = "y = " + str(c) + "*e^(x^2/2)"
                f = lambda x: c * math.e ** (x * x / 2)
                eq = lambda x, y: x * y
            elif tmp == 3:
                c = y0 / math.e ** x0 - x0
                f_as_text = "y = (" + str(c) + " + x) * e^x"
                f = lambda x: (c + x) * math.e ** x
                eq = lambda x, y: math.e ** x + y
            elif tmp == 4:
                c = (y0 - x0 ** 2 + 2 * x0 - 2) / math.e ** (-x0)
                f_as_text = "y = " + str(c) + "*e^(-x) + x^2 - 2x + 2"
                f = lambda x: c * math.e ** (-x) + x ** 2 - 2 * x + 2
                eq = lambda x, y: x ** 2 - y
            return eq, f, f_as_text
        except ValueError:
            handle_error("Ошибка ввода! Требуется ввести номер уравнения - целое число от 1 до 4.")


def input_n():
    while 1:
        print("Введите N - количество точек для метода Эйлера (целое число не меньше 2):")
        try:
            n = int(input())
            if n < 2:
                raise ValueError()
            return n
        except ValueError:
            handle_error("Ошибка ввода! Требуется ввести N - целое число не меньше 2.")


def input_b(x0):
    while 1:
        print("Введите B - правую границу для метода Эйлера (действительное число, больше X0, разделитель - точка):")
        try:
            b = float(input())
            if b <= x0:
                raise ValueError()
            return b
        except ValueError:
            handle_error("Ошибка ввода! Требуется ввести B - действительное число больше X0, разделитель - точка.")
