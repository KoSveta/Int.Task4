a=13.42
b=42.13
a1=int(a) #первые 2 цифры 1 числа
b1=int(b) #первые 2 цифры 2 числа

a2= int(a*100%100) #вторые 2 цифры 1 числа
b2= int(b*100%100) #вторые 2 цифры 2 числа

print(a1==b2 or a2==b1)

