from colorama import init, Fore, Style
init()

print(f"{Fore.YELLOW}{Style.BRIGHT} Вас приветсвуте программа по решение математических задач. \n\n{Style.RESET_ALL}")

def discriminat():
    a = float(input("Введите коэффициент a: "))
    if a == 0:
        print("Ошибка: коэффициент a не может быть равен 0 (уравнение не будет квадратным).")
        discriminat()
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
    elif discr < 0:
        print(f"{Fore.RED}{Style.BRIGHT}Корней нет.")
    input(f"{Fore.BLUE}{Style.BRIGHT}Нажмите Enter для завершения...{Style.RESET_ALL}")

def linear_equation():
    a = float(input("Введите коэффициент a: "))
    b = float(input("Введите коэффициент b: "))
    if a == 0:
        if b == 0:
            print("Бесконечно много решений.")
        else:
            print("Решений нет.")
    else:
        x = -b / a
        print("x =", x)
    input("Нажмите Enter для завершения...")

def main():
    print(f"\t{Fore.BLUE}{Style.BRIGHT}1. Вычеслить дискриминат и корни (ax² + bx + c = 0).\n",
      f"\t2. Решить линейное уравнение (ax + b = 0.).\n")
    choose = input(f"{Fore.YELLOW}Выберите опцию: ")
    if choose == "1":
        discriminat()
    elif choose == "2":
        linear_equation()
    else:
        print(f"{Fore.RED}Ввод был неверный, попробуйте снова.")

main()