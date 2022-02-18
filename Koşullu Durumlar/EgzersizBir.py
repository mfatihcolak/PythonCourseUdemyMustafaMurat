#Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

print("""
En büyük sayıyı bulalım
""")

a = int(input("1.sayıyı giriniz"))
b = int(input("2.sayıyı giriniz"))
c = int(input("3.sayıyı giriniz"))



if(a > b and a>c):
    print("En büyük sayı = {}".format(a))
elif(b> a and b>c):
    print("En büyük sayı = {}".format(b))
elif(c>a and c>b):
    print("En büyük sayı = {}".format(c))
else:
    print("sayılar eşit")
