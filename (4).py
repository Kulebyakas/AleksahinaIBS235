n = int(input("Введите число:")) 
if n < 1: 
 print("Ошибка") 
else: 
 x = 1 
 while (3 * x) < n: 
 x += 1 
 print(x)