from urllib.request import urlopen
edetabel = urlopen("https://ratings.fide.com/top.phtml?list=men")
baidid = edetabel.read()
tekst = baidid.decode()
eesnimi = str(input("Sisestage malemängja eesnimi: ")).lower()
perenimi = str(input("Sisestage malemängja perekonnanimi: ")).lower()
otsitav = perenimi.title() + ", " + eesnimi.title()
algus = tekst.index(otsitav)
rankkaks = tekst.index("Caruana, Fabiano")
temp_algus = algus + 53 + len(otsitav)  
elo = tekst[temp_algus:temp_algus+4]
i = 9266
rank = 0
while i < algus:
    i += 225
    rank += 1
print(elo)
print(rank)
