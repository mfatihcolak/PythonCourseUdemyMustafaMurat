boy = float(input("Lütfen boyunuzu giriniz ör.(1.87)"))
kilo = int(input("Lütfen kilonuzu giriniz"))

bmi = (kilo) / (boy * boy)

print("Beden Kitle İndeksiniz = ",bmi)

if bmi < 18.5:
    print("Zayıfsınız")
elif bmi > 18.5 and bmi < 25:
    print("Normal kilodasınız")
elif bmi > 25 and bmi < 30:
    print("Fazla Kilolusunuz")
elif bmi > 30:
    print("Obezsiniz")
    