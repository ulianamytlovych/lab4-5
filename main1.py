import math

def calculate_sum(a, b, epsilon):
    z = 0
    n = 0
    term = 1 
    
    while abs(term) >= epsilon:
        term = ((a ** 2 + b ** 2) ** 0.5) - z  
        z += term  
        n += 1
    
    return z, n 

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
epsilon = float(input("Введіть точність ε: "))

result, iterations = calculate_sum(a, b, epsilon)

print(f"Обчислене значення z: {result}")
print(f"Кількість ітерацій: {iterations}")
