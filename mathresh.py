from colorama import init, Fore, Style
import time
import shutil

init()

def print_centered(text):
    terminal_width = shutil.get_terminal_size().columns
    print(text.center(terminal_width))

print_centered(f"{Fore.GREEN}{Style.BRIGHT}Вас приветствует программа по решению математических задач.{Style.RESET_ALL}")

def discriminat():
    while True:
        try:
            a = float(input(f"{Fore.YELLOW}{Style.BRIGHT}Введите коэффициент a: {Style.RESET_ALL}"))
            if a == 0:
                print(f"{Fore.RED}{Style.BRIGHT}Ошибка: коэффициент a не может быть равен 0 (уравнение не будет квадратным).{Style.RESET_ALL}")
                continue
            break
        except ValueError:
            print(f"{Fore.RED}{Style.BRIGHT}Ошибка: введите корректное число.{Style.RESET_ALL}")
    try:
        b = float(input(f"{Fore.YELLOW}{Style.BRIGHT}Введите коэффициент b: {Style.RESET_ALL}"))
        c = float(input(f"{Fore.YELLOW}{Style.BRIGHT}Введите коэффициент c: {Style.RESET_ALL}"))
        discr = b ** 2 - 4 * a * c
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Дискриминант = {discr}{Style.RESET_ALL}")
        if discr > 0:
            x1 = (-b + (discr) ** 0.5) / (2 * a)
            x2 = (-b - (discr) ** 0.5) / (2 * a)
            print(f"{Fore.GREEN}{Style.BRIGHT}x1 = {x1}, x2 = {x2}{Style.RESET_ALL}")
        elif discr == 0:
            x = -b / (2 * a)
            print(f"{Fore.GREEN}{Style.BRIGHT}x = {x}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}Корней нет.{Style.RESET_ALL}")
        input(f"{Fore.BLUE}{Style.BRIGHT}Нажмите Enter для продолжения...{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}{Style.BRIGHT}Ошибка: введите корректное число.{Style.RESET_ALL}")
        input(f"{Fore.BLUE}{Style.BRIGHT}Нажмите Enter для продолжения...{Style.RESET_ALL}")

def viet():
    try:
        a = float(input(f"{Fore.YELLOW}{Style.BRIGHT}Введите коэффициент a: {Style.RESET_ALL}"))
        if a == 0:
            print(f"{Fore.RED}{Style.BRIGHT}Ошибка: коэффициент a не может быть равен 0 (уравнение не будет квадратным).{Style.RESET_ALL}")
            input(f"{Fore.BLUE}{Style.BRIGHT}Нажмите Enter для продолжения...{Style.RESET_ALL}")
            return
        b = float(input(f"{Fore.YELLOW}{Style.BRIGHT}Введите коэффициент b: {Style.RESET_ALL}"))
        c = float(input(f"{Fore.YELLOW}{Style.BRIGHT}Введите коэффициент c: {Style.RESET_ALL}"))
        discr = b ** 2 - 4 * a * c
        if discr > 0:
            x1 = (-b - (discr) ** 0.5) / (2 * a)
            x2 = (-b + (discr) ** 0.5) / (2 * a)
            print(f"{Fore.CYAN}{Style.BRIGHT}По теореме Виета:")
            print(f"\tКорень x1 = {x1}")
            print(f"\tКорень x2 = {x2}{Style.RESET_ALL}")

            print(f"{Fore.MAGENTA}{Style.BRIGHT}Проверка:\n \tСумма корней = {-b/a},\n \tПроизведение корней = {c/a}{Style.RESET_ALL}")
        elif discr == 0:
            x = -b / (2 * a)
            print(f"{Fore.CYAN}{Style.BRIGHT}По теореме Виета:")
            print(f"Корень x = {x}{Style.RESET_ALL}")
            print(f"Проверка:\n \tСумма корней = {-b/a},\n \tПроизведение корней = {c/a}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}Дискриминант отрицательный, реальных корней нет.{Style.RESET_ALL}")
        input(f"{Fore.BLUE}{Style.BRIGHT}Нажмите Enter для продолжения...{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}{Style.BRIGHT}Ошибка: введите корректное число.{Style.RESET_ALL}")
        input(f"{Fore.BLUE}{Style.BRIGHT}Нажмите Enter для продолжения...{Style.RESET_ALL}")

def linear_equation():
    print(f"{Fore.GREEN}{Style.BRIGHT}\nВыберите вариант решения:")
    print(f"\t1. ax + b = 0")
    print(f"\t2. ax - b = 0{Style.RESET_ALL}")
    choose = input(f"{Fore.GREEN}{Style.BRIGHT}Ваш выбор: {Style.RESET_ALL}")
    if choose not in ["1", "2"]:
        print(f"{Fore.RED}{Style.BRIGHT}Введен неверный вариант.\n{Style.RESET_ALL}")
        return
    try:
        a = float(input(f"{Fore.YELLOW}{Style.BRIGHT}Введите коэффициент a: {Style.RESET_ALL}"))
        b = float(input(f"{Fore.YELLOW}{Style.BRIGHT}Введите коэффициент b: {Style.RESET_ALL}"))
        if a == 0:
            if b == 0:
                print(f"\t{Fore.GREEN}{Style.BRIGHT}Бесконечно много решений.{Style.RESET_ALL}")
            else:
                print(f"\t{Fore.RED}{Style.BRIGHT}Решений нет.{Style.RESET_ALL}")
        else:
            if choose == "1":
                x = -b / a
                print(f"\t{Fore.GREEN}{Style.BRIGHT}x = {x}{Style.RESET_ALL}")
            elif choose == "2":
                x = b / a
                print(f"\t{Fore.GREEN}{Style.BRIGHT}x = {x}{Style.RESET_ALL}")
        input(f"{Fore.BLUE}{Style.BRIGHT}Нажмите Enter для продолжения...{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}{Style.BRIGHT}Ошибка: введите корректное число.{Style.RESET_ALL}")
        input(f"{Fore.BLUE}{Style.BRIGHT}Нажмите Enter для продолжения...{Style.RESET_ALL}")

def factorial():
    try:
        n = int(input(f"{Fore.YELLOW}{Style.BRIGHT}Введите неотрицательное целое число для вычисления факториала: {Style.RESET_ALL}"))
        if n < 0:
            print(f"{Fore.RED}{Style.BRIGHT}Ошибка: факториал определён только для неотрицательных чисел.{Style.RESET_ALL}")
        else:
            result = 1
            for i in range(1, n + 1):
                result *= i
            print(f"{Fore.GREEN}{Style.BRIGHT}{n}! = {result}{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}{Style.BRIGHT}Ошибка: введите целое число.{Style.RESET_ALL}")
    input(f"{Fore.BLUE}{Style.BRIGHT}Нажмите Enter для продолжения...{Style.RESET_ALL}")
def main():
    while True:
        print(f"\n\n\t{Fore.BLUE}{Style.BRIGHT}0. Выйти из программы.\n"
              f"\t1. Вычислить дискриминант и корни из ax² + bx + c = 0.\n"
              f"\t2. Теорема Виета для ax² + bx + c = 0.\n"
              f"\t3. Решить линейное уравнение (ax + b = 0 или ax - b = 0).\n"
              f"\t4. Вычислить факториал (n!).\n{Style.RESET_ALL}")
        choose = input(f"{Fore.YELLOW}{Style.BRIGHT}Выберите опцию: {Style.RESET_ALL}")
        if choose == "0":
            print(f"{Fore.CYAN}{Style.BRIGHT}До свидания!{Style.RESET_ALL}")
            time.sleep(2)  
            exit()
        elif choose == "1":
            discriminat()
        elif choose == "2":
            viet()
        elif choose == "3":
            linear_equation()
        elif choose == "4":
            factorial()
        else:
            print(f"{Fore.RED}{Style.BRIGHT}Ввод был неверный, попробуйте снова.{Style.RESET_ALL}")

main()