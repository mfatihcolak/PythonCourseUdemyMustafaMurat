class Dosya():
    def __init__(self):
        with open("metin.txt","r",encoding="utf-8")as file:
            dosyaIcerigi = file.read()
            print(dosyaIcerigi)
            kelimeler = dosyaIcerigi.split()
            self.sadelestirilmis = list()
            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip("")
                i = i.strip(".")
                i = i.strip(",")
                self.sadelestirilmis.append(i)
    def tumKelimeler(self):
        kelimelerKumesi = set()
        for i in self.sadelestirilmis:
            kelimelerKumesi.add(i)
        print("Tüm Kelimeler...")

        for i in  kelimelerKumesi:
            print(i)
            print("----------")
    def kelimeFrekansi(self):
        kelimeSozluk = dict()
        for i in self.sadelestirilmis:
            if (i in kelimeSozluk):
                kelimeSozluk[i] +=1
            else:
                kelimeSozluk[i] = 1
        for kelime,sayi in kelimeSozluk.items():
            print("{} kelimesinden {} tane var...".format(kelime,sayi))
dosya = Dosya()

dosya.kelimeFrekansi()
