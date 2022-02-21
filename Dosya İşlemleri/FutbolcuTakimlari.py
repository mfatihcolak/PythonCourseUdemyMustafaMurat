fenerbahce = []
galatasaray = []
besiktas = []

def takimAyir(satir):
    satir = satir[:-1]
    liste = satir.split(",")
    oyuncu = liste[0]
    takim = liste[1]

    if(takim == "galatasaray"):
        galatasaray.append(satir +"\n")
    elif(takim == "beşiktaş"):
        besiktas.append(satir +"\n")
    elif(takim == "fenerbahçe"):
        fenerbahce.append(satir +"\n")

    return "Oyuncunun Adı : " + oyuncu + "Takımı : " + takim

with open("futbolcular.txt","r",encoding="utf-8") as file:
    oku = []
    for i in  file:
        oku.append(takimAyir(i))
    print(oku)

    with open("galatasaray.txt","w",encoding ="utf-8") as file2:
        for i in galatasaray:
            file2.write(i)
    with open("fenerbahce.txt","w",encoding="utf-8")as file3:
        for i in fenerbahce:
            file3.write(i)
    with open("besiktas.txt","w",encoding="utf-8") as file4:
        for i in besiktas:
            file4.write(i)