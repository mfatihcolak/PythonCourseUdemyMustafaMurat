a = int(input("Lütfen bir sayı girin armstrong sayımı bulalım: "))

b = len(str(a))

if(b == 3):
    birler = a // 100
    onlar = (a // 10) % 10
    yuzler = a % 10

    if ((birler **3)+(onlar**3)+(yuzler**3) == a):
        print(a, " bir armstrong sayıdır..")
    else:
        print(a, " bir mükemmel sayı değildir..")

elif(b == 4):
    birler = a // 1000
    onlar = (a // 10) % 10
    yuzler = (a // 100) % 10
    binler = a % 10
    if((birler **4)+(onlar**4)+(yuzler**4)+(binler**4) == a):
        print(a ," bir armstrong sayıdır..")
    else:
        print(a, "bir armstrong sayı değildir..")