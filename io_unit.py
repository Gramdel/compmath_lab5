import math


def handle_error(msg):
    print(msg)
    print("Enter = повторить ввод, любая другая клавиша + Enter = выход:")
    tmp = input()
    if tmp == "":
        return
    print("Программа завершает работу.")
    quit(-1)


def choose_func(f=None, f_as_text=None, x=None, y=None):
    f_list = ["y = x", "y = x^2", "y = lg(x)", "y = sin(x)"]
    print("Программа умеет работать со следующими функциями:")
    for i in range(len(f_list)):
        print(str(i+1) + ". " + f_list[i])
    while 1:
        print("Введите номер нужной функции (целое число от 1 до 4):")
        try:
            tmp = int(input())
            if (tmp < 1) | (tmp > 4):
                raise ValueError()
            elif tmp == 1:
                f = lambda x: x
                x = [-5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
                y = [-5, -4.5, -3.5, -3.5, -3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
            elif tmp == 2:
                f = lambda x: x * x
                x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
                y = [25, 16, 9, 4, 1, 0, 1, 4, 6, 16, 25]
            elif tmp == 3:
                f = lambda x: math.log10(x)
                x = [0.3, 0.5, 1, 2, 3, 4, 5]
                y = [-0.5, -0.3, 0, 0.3, 0.4, 0.6, 0.7]
            elif tmp == 4:
                f = lambda x: math.sin(x)
                x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
                y = [0.95, 0.75, 0.2, -0.9, -0.84, 0, 0.84, 0.9, 0.14, -0.75, -0.95]
            f_as_text = f_list[tmp - 1]
            return f, f_as_text, x, y
        except ValueError:
            handle_error("Ошибка ввода! Требуется ввести номер функции - целое число от 1 до 4.")
