cumle = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

def cumleFrekans():
    harf = dict()
    for i in cumle:
        if (i in harf):
            harf[i] +=1
        else:
            harf[i] = 1
    for harfadet,sayi in harf.items():
        print("{} harfi yukaridaki cümlede {}tane var".format(harfadet,sayi))

cumleFrekans()