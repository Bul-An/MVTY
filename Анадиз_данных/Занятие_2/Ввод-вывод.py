#ВЫВОД ДАННЫХ
x = 3
y = 5.6

# вывод значений x и y в одну строку, через пробел
print(x, y)

#Следующие 2 оператора выведут значения x и Y в две строки
print(x)
print(y)

#Следующие 2 оператора выведут значения x и Y в одну строку, через пробел
print(x, end=' ')
print(y)

#Вывод значений x и y в одну строку через точку с запятой
print(x, y, sep=';')

#Форматированный вывод
print(f"Значение х: {x}, значение y:{y}")

#Форматированный вывод с выравниванием влево в поле шириной 9 знаков
print(f"x:{x: <9}|y:{y: <9}|")

#Форматированный вывод с выравниванием вправо в поле шириной 9 знаков
print(f"x:{x: >9}|y:{y: >9}|")

#Форматированный вывод с выравниванием по центру в поле шириной 9 знаков
print(f"x:{x: ^9}|y:{y: ^9}|")

#Форматированный вывод с выравниванием влево в поле шириной 9 знаков
#Значение y выводится с точростью 2 знака после запятой
print(f"x:{x: ^9}|y:{y: ^9.2f}|")

#ВВОД ДАННЫХ

#Ввод одного целого числа из консоли
x = int(input())

#Ввод одной десятичрной дроби из консоли
x = float(input())

#Ввод двух целых чисел расположенных в одной строке и разделённых пробелом
x, y = map(int, input().split())

#Ввод неопределённого количества целых чисел расположенных в одной строке и разделённых запятой
#Результатом ввода будет список
z = list(map(int, input().split(',')))

#Ввод одной строки из файла
fin = open('../Primer.txt')
s = fin.readline()

#Ввод нескольких строк из файла. Создание списка строк
fin = open('../Primer.txt')
s = []

for item in fin:
    s.append(item)

#Ввод целых чисел из текстового файла. Числа расположены по одному в каждой строке. Создание списка целых чисел
fin = open('../Primer.txt')
array = []

for item in fin:
    x = int(item)
    array.append(x)

#Ввод целых чисел из текстового файла. Числа расположены по два в каждой строке. Создание списка кортежей.
fin = open('../Primer.txt')
array = []

for item in fin:
    x, y = map(int, item.split())
    array.append((x, y))

#Вывод списка целых чисел в файл, по одному значению в каждую строку.
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fout = open('../Primer1.txt', 'w')
for i in range(0, len(array)):
    fout.write(str(array[i]) + '\n')








