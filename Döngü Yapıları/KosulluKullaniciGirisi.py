print("""
****************
KULLANICI GİRİŞ EKRANI
****************
""")
kayitli_ad = "fatih"
kayitli_parola = "12345"

giris_hakki = 3

while True:
    kullanici_adi = input("Kullanıcı Adı: ")
    parola = input("Parola: ")
    if (kayitli_ad != kullanici_adi and kayitli_parola == parola):
        print("Kullanıcı adı hatalı")
        giris_hakki -=1
        print("Kalan giriş hakkınız = {}".format(giris_hakki))
    elif (kayitli_ad == kullanici_adi and kayitli_parola != parola):
        print("Parola hatalı")
        giris_hakki -= 1
        print("Kalan giriş hakkınız = {}".format(giris_hakki))
    elif (kayitli_ad != kullanici_adi and kayitli_parola != parola):
        print("Kullanıcı Adı ve Parola hatalı")
        giris_hakki -= 1
        print("Kalan giriş hakkınız = {}".format(giris_hakki))
    else:
        print("Giriş Başarılı - Hoşgeldiniz")
        break
    if(giris_hakki == 0):
        print("Giriş hakkınız bitti")
        break