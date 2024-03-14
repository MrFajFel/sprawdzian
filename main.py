ilosc_Parzystych = 0
tyle_Samo = 0
same_Zera = 0
same_Jedynki = 0
zakonczenie = 1
with open("napisy.txt") as plik:
    for i in range(len(plik.readline())):
        linijka = plik.readline()
# a.
        if len(linijka) % 2 == 0:
            ilosc_Parzystych += 1
    # b.
        if linijka == plik.readline():
            tyle_Samo += 1
    # c.
        if len(linijka) != 1:
            same_Zera += 1
        if len(linijka) != 0:
            same_Jedynki += 1
    # d.
        for i in range(len(linijka)):
            if linijka[-1] == zakonczenie:
                print("konczy sie 1:" + linijka)
        #e.
        od_Tylu = "".join(reversed(linijka))
        if od_Tylu == linijka:
            print("palindrom:"+od_Tylu +" "+ linijka)
        #f.
        for k in range(0,17):
            if k == len(linijka):
                print("K rowne: "+str(k-1)+" "+linijka)

    print("tyle jest parzystych:"+str(ilosc_Parzystych))
    print("tyle jest napisow takich takich samych:"+str(tyle_Samo))
    print("Tyle bylo samych Jedynek:" + str(same_Jedynki))
    print("Tyle jest samych zer:"+str(same_Zera))