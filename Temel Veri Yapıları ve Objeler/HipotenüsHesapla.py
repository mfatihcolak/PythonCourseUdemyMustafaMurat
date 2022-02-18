import math

print("""
HİPOTENÜS HESAPLAMA PROGRAMINA HOŞGELDİNİZ
""")

kenar_a = float(input("Lütfen A kenarını giriniz : "))
kenar_b = float(input("Lütfen B kenarını giriniz : "))

hipotenüs = (kenar_a ** 2) + (kenar_b **2)
kenar_hipo = math.sqrt(hipotenüs)

print("Hipotenüs = " , kenar_hipo)