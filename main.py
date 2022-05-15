from numpy import arange
import matplotlib.pyplot as plt
from io_unit import choose_eq
from io_unit import input_point
from io_unit import input_n
from io_unit import input_b


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


def euler_method(x_values, y_values, eq, n, b):
    h = (b - x_values[0]) / n
    for i in range(1, n + 1):
        x_values.append(x_values[0] + i * h)
        y_values.append(y_values[-1] + h * eq(x_values[-1], y_values[-1]))
    return x_values, y_values


def show_plot(x_values, y_values, true_x_values, true_y_values, newton_y_values, f_as_text):
    fig, ax = plt.subplots()
    ax.plot(true_x_values, true_y_values, color="green", label=f_as_text)
    ax.plot(true_x_values, newton_y_values, color="red", label="Полином")
    for i in range(len(x_values)):
        plt.plot(x_values[i], y_values[i], "ro", markersize=4)
    ax.grid()
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend(loc=4)
    plt.show()


def main():
    print("Вас приветствует программа для демонстрации решения задачи Коши методом Эйлера!")
    x0, y0 = input_point()
    eq, f, f_as_text = choose_eq(x0, y0)
    n = input_n()
    b = input_b(x0)

    x_values, y_values = euler_method([x0], [y0], eq, n, b)

    newton_pol = create_newton_polynomial(x_values, y_values)
    delta = 0 if x_values[1] - x_values[0] < 0.01 else 0.01
    true_x_values = arange(x_values[0], x_values[-1] + delta, delta)
    true_y_values = []
    newton_y_values = []
    for i in true_x_values:
        true_y_values.append(f(i))
        newton_y_values.append(newton_pol(i))

    show_plot(x_values, y_values, true_x_values, true_y_values, newton_y_values, f_as_text)


main()
