basHarfler = ""
with open("Şiir.txt","r",encoding="utf-8") as file:
    for satir in file:
        basHarfler += satir[0]
print(basHarfler)
print(satir)