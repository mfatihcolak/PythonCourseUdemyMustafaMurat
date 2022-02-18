#arabanın kilometrede ne kadar yaktığını hesaplama

depo = int(input("Aracnınızın deposu kaç litre yakıt alıyor"))
litre_fiyati = float(input("Aldığınız yakıtın litre fiyatı nedir"))
menzil = int(input("Full depo yakıt ile kaç km gidiyorsunuz"))

maliye = (depo * litre_fiyati) / menzil

print("Aracınız km'de ", maliye, "kuruş yakıyor")
