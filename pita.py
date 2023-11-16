f = open("forras.txt", "r", encoding="utf8")
lines = f.readlines()
f.close()

diakok = []
for line in lines:
    line = line.strip()
    parts = line.split(";")
    diak = {
        "id" : int(parts[0]),
        "nev" : parts[1]
    }
    diakok.append(diak)


f2 = open("jegyek.txt","r", encoding="utf8")
lines2 = f2.readlines()
f2.close()

jegyek=[]
for line in lines2:
    line = line.strip()
    parts2 = line.split(";")
    jegy={
        "id" : int(parts2[0]),
        "jegyek" : parts2[1]
    }
    jegyek.append(jegy)

diakinput = input("Név: ")
keresett = None
for diak in diakok:
    if diak["nev"] == diakinput:
        keresett = diak
        break
if keresett != None:
    print(keresett["id"])
    for adat in jegyek:
        if adat["id"] == keresett["id"]:
            print(f"Jegyek: {adat["jegyek"]}")
            break
else:
    print("Nincs ilyen diák!")