#map fonksiyonu

def alan(demet):
    return demet[0]*demet[1]

liste = [(3,4),(10,3),(5,6),(1,9)]

print(list(map(alan,liste)))

sayilar = [*range(1,50)]

a = [*map(lambda x : x /2,sayilar)]
print(a)