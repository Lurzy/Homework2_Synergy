# Задание номер 1. Пользователь вводит стороны прямоугольника, выведите его площадь и периметр. На вход программе могут подаваться как целые числа, так и вещественные

print("Введите ширину и длину прямоугольника:")
a, b = map(int, input().split())
square = a * b
perimeter = (a+b)*2
print("Площадь прямоугольника равна: ", square)
print("Периметр прямоугольника равен: ", perimeter)
