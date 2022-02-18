def ebob():
    tamBolenA = []
    tamBolenB = []
    ortakBolen = []
    a = int(input("Lütfen ilk sayıyı giriniz: "))
    b = int(input("Lütfen ikinci sayıyı giriniz: "))
    for i in range(1,a+1):
        if(a%i == 0):
            tamBolenA.append(i)

    for i in range(1,b+1):
        if(b%i == 0):
            tamBolenB.append(i)

    for eleman in tamBolenA:
        if eleman in tamBolenB:
            ortakBolen.append(eleman)

    EBOB = max(ortakBolen)
    EKOK = (a*b)//EBOB

    return print("Ebob = ",EBOB,"Ekok = ",EKOK,"Ortak bölenler = ",ortakBolen)






