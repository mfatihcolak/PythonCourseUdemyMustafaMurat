print("Dörtgen mi? Üçgen mi?")

print("Kaç kenarlı ?")

kenar = input("Dörtgen or Üçgen ")

if kenar == "dörtgen":
    a = int(input("1.kenarı giriniz:"))
    b = int(input("2.kenarı giriniz:"))
    c = int(input("3.kenarı giriniz:"))
    d = int(input("4.kenarı giriniz:"))

    if  a == b == c == d :
        print("GİRDİĞİNİZ DÖRTGEN BİR KAREDİR")
    elif a == b and c == d :
        print("Girdiğiniz dörtgen bir dikdortgen")
    else:
        print("sıradan bir dörtgen")
elif kenar == "üçgen":

    a = int(input("1.kenarı giriniz:"))
    b = int(input("2.kenarı giriniz:"))
    c = int(input("3.kenarı giriniz:"))

    if a == b and b==c and a==c:
        print("Girdiğiniz üçgen bir eşkenar üçgendir")
    elif (a == b or b == c or a == c) :
        print("Girdiğiniz üçgen bir ikizkenar üçgendir")
    elif (a+b) <=c or (a+c) <= b or (b+c) <= a:
        print("Girdiğiniz kenarlar bir üçgen belirtmez")
    else:
        print("sıradan üçgen")
