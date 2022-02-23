isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyIsimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

adSoyad = [*zip(isimler,soyIsimler)]
adSoyad.sort()
for i,j in adSoyad:
    print(i,j)