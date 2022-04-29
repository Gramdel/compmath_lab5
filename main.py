from numpy import arange
import matplotlib.pyplot as plt
from io_unit import choose_func


def divided_differences(x_values, y_values, k):
    result = 0
    for j in range(k + 1):
        mul = 1
        for i in range(k + 1):
            if i != j:
                mul *= x_values[j] - x_values[i]
        result += y_values[j] / mul
    return result


def create_newton_polynomial(x_values, y_values):
    div_diff = []
    for i in range(1, len(x_values)):
        div_diff.append(divided_differences(x_values, y_values, i))

    def newton_polynomial(x):
        result = y_values[0]
        for k in range(1, len(y_values)):
            mul = 1
            for j in range(k):
                mul *= (x - x_values[j])
            result += div_diff[k - 1] * mul
        return result

    return newton_polynomial


def show_plot(x, y, clear_x, clear_y, f_as_text):
    fig, ax = plt.subplots()
    ax.plot(x, y, color="red", label="Полином")
    ax.plot(clear_x, clear_y, color="green", label=f_as_text)
    ax.grid()
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend(loc=4)
    plt.show()


def main():
    print("Вас приветствует программа для демонстрации метода интерполяции полиномом Ньютона!")
    f, f_as_text, x, y = choose_func()
    clear_x = arange(x[0], x[len(x) - 1] + 0.1, 0.1)
    clear_y = []
    for i in clear_x:
        clear_y.append(f(i))

    newton_pol = create_newton_polynomial(x, y)
    newton_y = []
    for i in clear_x:
        newton_y.append(newton_pol(i))

    show_plot(clear_x, newton_y, clear_x, clear_y, f_as_text)


main()
