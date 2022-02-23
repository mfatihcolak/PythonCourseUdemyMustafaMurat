mail = []
mailler = []

with open("mailler.txt", "r", encoding="utf-8") as file:
    for i in file:
        i = i[:-1]
        mail.append(i)
    for i in mail:
        if i.endswith(".com") and i.find("@") != -1:
            mailler.append(i)
print(mailler)