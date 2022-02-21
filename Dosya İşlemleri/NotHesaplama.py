kalanlar = []
gecenler = []
aaAlanlar = []
def NotHesapla(satir):
    satir = satir[:-1]
    liste = satir.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste [2])
    not3 = int(liste[3])

    sonNot = not1 * (3/10) + not2 *(3/10)+ not3 *(4/10)

    if (sonNot >= 90):
        harf = "AA"
        aaAlanlar.append(isim + "---->" + "Not Ort." + str(sonNot) + "---->" + harf + "\n")
    elif(sonNot >= 85):
        harf = "BA"
    elif (sonNot >= 80):
        harf = "BB"
    elif (sonNot >= 75):
        harf = "CB"
    elif (sonNot >= 70):
        harf = "CC"
    elif (sonNot >= 65):
        harf = "DC"
    elif (sonNot >= 60):
        harf = "DD"
    elif (sonNot >= 55):
        harf = "FD"
    else:
        harf = "FF"
    if(sonNot >= 55):
        gecenler.append(isim + "---->" + "Not Ort." + str(sonNot) + "---->"+harf+"\n")
    else:
        kalanlar.append(isim + "---->" + "Not Ort." + str(sonNot) + "---->"+harf+"\n")


    return  isim +"-------------->"+ harf+"\n"



with open("dosya.txt","r",encoding="utf-8") as file:
    ekleneceklerListesi = []

    for i in file:
        ekleneceklerListesi.append(NotHesapla(i))

    print(ekleneceklerListesi)

    with open("notlar.txt","w",encoding="utf-8") as file2:
        for i in ekleneceklerListesi:
            file2.write(i)

    with open("kalanlar.txt","w",encoding="utf-8") as file3:
        for i in kalanlar:
            file3.write(i)
    with open("gecenler.txt","w",encoding="utf-8") as file4:
        for i in gecenler:
            file4.write(i)

    with open("AAalanlar.txt","w",encoding="utf-8") as  file5:
        for i in aaAlanlar:
            file5.write(i)