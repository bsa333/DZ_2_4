#Вычислить число Pi c заданной точностью d, не используя ф. round()
import os
os.system('cls' if os.name == 'nt' else 'clear')
from math import pi

num = int(input("Введите число для заданной точности числа Пи:\n"))
stroka = str(pi)
print(float(stroka[0:num+2]))
