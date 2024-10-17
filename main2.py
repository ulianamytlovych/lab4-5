import math

def tabulate_prog(a, b, h, z):
    count_exceed = 0  
    r = a
    
    while r <= b:
        suma = (4 / 3) * math.pi * r ** 3
        print(f"r = {r:.2f}, S = {suma:.2f}")
        
        if suma > z:
            count_exceed += 1
            if count_exceed == 2:
                print("Табулювання припинено: Два значення перевищили число z.")
                break
        
        r += h 
a = float(input("Введіть початкове значення a: "))
b = float(input("Введіть кінцеве значення b: "))
h = float(input("Введіть крок h: "))
z = float(input("Введіть значення z: "))

tabulate_prog(a, b, h, z)  

