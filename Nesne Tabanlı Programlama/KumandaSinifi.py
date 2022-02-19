import random
import time


class Kumanda():

    def __init__(self, tvDurum="Kapalı", tvSes=0, kanalListesi=["TRT"], kanal="Trt"):
        self.tvDurum = tvDurum
        self.tvSes = tvSes
        self.kanalListesi = kanalListesi
        self.kanal = kanal

    def tvAc(self):
        if (self.tvDurum == "Açık"):
            print("TV zaten açık")
        else:
            print("TV açılıyor")
            self.tvDurum = "Açık"

    def tvKapat(self):
        if (self.tvDurum == "Kapalı"):
            print("TV zaten kapalı")
        else:
            print("TV kapanıyor")
            self.tvDurum == "Kapalı"

    def sesAyarlari(self):
        while True:
            cevap = input("Sesi Azalt = '-' \nSesi Artır = '+' \nÇıkış = 'çıkış'")

            if (cevap == "-"):
                if (self.tvSes != 0):
                    self.tvSes -= 1
                    print("Ses = ", self.tvSes)
            elif (cevap == "+"):
                if (self.tvSes != 31):
                    self.tvSes += 1
                    print("Ses = ", self.tvSes)
            else:
                print("Ses = ", self.tvSes)
                break

    def kanalEkle(self, kanalIsmi):
        print("Kanal Ekleniyor")
        time.sleep(1)
        self.kanalListesi.append(kanalIsmi)
        print("Kanal Eklendi")

    def rastgeleKanal(self):
        rastgele = random.randint(0, len(self.kanalListesi) - 1)
        self.kanal = self.kanalEkle(rastgele)
        print("Şuanki kanal:", self.kanal)

    def __len__(self):
        return len(self.kanalListesi)

    def __str__(self):
        return "TV durumu: {} \nTV Ses: {} \nŞuanki Kanal: {} \n".format(self.tvDurum, self.tvSes, self.kanal)


kumanda = Kumanda()

print("""
TELEVİZYON UYGULAMASI
1-TV AÇ
2-TV KAPAT
3-SES AYARLARI
4-KANAL EKLE
5-KANALLAR
6-KANAL DEĞİŞ
7-TV BİLGİLERİ
ÇIKIŞ İÇİN q'a BASIN
""")
while True:
    islem = input("İşlemi Seçin:")

    if (islem == "q"):
        print("Program sonlandırılıyor")
        break
    elif (islem == "1"):
        kumanda.tvAc()
    elif (islem == "2"):
        kumanda.tvKapat()
    elif (islem == "3"):
        kumanda.sesAyarlari()
    elif (islem == "4"):
        kanalIsımleri = input("Kanal isimlerini ',' ile ayırarak girin")
        kanalListesi = kanalIsımleri.split(",")
        for eklenecekler in kanalListesi:
            kumanda.kanalEkle(eklenecekler)
    elif (islem == "5"):
        print("Kanal Sayısı = ", len(kumanda))
        print("Kanallar = ",kumanda.kanalListesi)
    elif (islem == "6"):
        kumanda.rastgeleKanal()
    elif (islem == "7"):
        print(kumanda)
    else:
        print("YANLIŞ İŞLEM !")
