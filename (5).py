n = int(input("Введите число:")) 
if n < 1: 
 print("Ошибка") 
else: 
 x = 10000 
 while (3*x)>n: 
 x=x-1 
print(x)