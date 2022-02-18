print("""
**************
Giriş Ekranı
**************
""")
kullanici_adi = "murat"
parola = "12345"

k_adi = input("Kullanıcı Adı :")
k_parola = input("Parola :")

if (kullanici_adi == k_adi and parola != k_parola):
    print("Parola Hatalı")
elif(kullanici_adi != k_adi and parola == k_parola):
    print("Kullanıcı Adı Hatalı")
elif(kullanici_adi != k_adi and parola != k_parola):
    print("Kullanıcı Adı ve Parola Hatalı")
else:
    print("Giriş Başarılı")
