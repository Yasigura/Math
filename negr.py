#penis
from tkinter import ttk
from tkinter import *

root = tkk()
a = float (input('Введите коэфициент a:'))
b = float (input('Введите коэфициент b:'))
c = float (input('Введите коэфициент c:'))
discr = b**2 - 4*a*c
print('Дискрименант =', discr)
if discr > 0:
    print('Есть два корня:')
    x1 = (-b + discr**0.5) / (2*a)
    x2 = (-b - discr**0.5) / (2*a)
    print('Первый корень:', x1)
    print('Второй корень:', x2)
elif discr == 0:
    print('Есть один корень:')
    x = -b / (2*a)
    print('Один корень:', x) 
elif discr < 0:
    print('Корней нет.')
input ()


root.mainloop()
