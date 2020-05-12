from urllib.request import urlopen
edetabel = urlopen("https://ratings.fide.com/top.phtml?list=men")
baidid = edetabel.read()
tekst = baidid.decode()
eesnimi = str(input("Sisestage malemängja eesnimi: ")).lower()
perenimi = str(input("Sisestage malemängja perekonnanimi: ")).lower()
otsitav = perenimi.title() + ", " + eesnimi.title()
algus = tekst.index(otsitav)
temp_algus = algus + 53 + len(otsitav)  
elo = tekst[temp_algus:temp_algus+4]       
print(elo)