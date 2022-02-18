a = int(input("Bir sayı girin mükemmel sayımı kontrol edelim : "))
total = 0



for i in range(1,a):
    if(a%i == 0 ):
        total +=i
if(total == a):
    print(a," Mükemmel sayı")
else:
    print(a," mükemmel sayı değildir")