import math

def suma_p(x, y, a, b, N):
    sum_value = 0  
    i = 0 

    while i < N:
        term = (x**2 / (a**2)) - (y**2 / (b**2))  
        sum_value += term  
        i += 1  
    return sum_value  

x = float(input("Введіть значення x: "))  
y = float(input("Введіть значення y: "))  
a = float(input("Введіть значення a: "))  
b = float(input("Введіть значення b: "))
N = int(input("Введіть кількість членів ряду N: "))  

result = suma_p(x, y, a, b, N)
print(f"Сума перших {N} членів послідовності = {result}")

