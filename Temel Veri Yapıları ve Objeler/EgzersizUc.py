#Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin

a = int(input("a:"))
b = int(input("b:"))

gecici = a
a = b
b = gecici

print(a,b)
