

def test():
    a = float(input("Введите коэффициент a: "))
    if a == 0:
        print("Ошибка: коэффициент a не может быть равен 0 (уравнение не будет квадратным).")
        input("Нажмите Enter для завершения...")
        return
    b = float(input("Введите коэффициент b: "))
    c = float(input("Введите коэффициент c: "))
    discr = b ** 2 - 4 * a * c
    print("Дискриминант =", discr)
    if discr > 0:
        x1 = (-b + (discr) ** 0.5) / (2 * a)
        x2 = (-b - (discr) ** 0.5) / (2 * a)
        print("x1 =", x1, "x2 =", x2)
    elif discr == 0:
        x = -b / (2 * a)
        print("x =", x)
    else:  # discr < 0
        print("Корней нет.")
    input("Нажмите Enter для завершения...")


if __name__ == "__main__":
    test()