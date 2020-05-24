from urllib.request import urlopen

edetabel = urlopen("https://ratings.fide.com/top.phtml?list=men")
baidid = edetabel.read()
tekst = baidid.decode()

asukoht = str(input("Sisestage malemängja asukoht edetabelis: ")).lower()

otsitav = "<td width=10>&nbsp;" + asukoht + "</a></td>"
algus = tekst.index(otsitav)

sisaldabnime = tekst[algus:algus+200]
nimi = sisaldabnime[sisaldabnime.index("class=tur")+len("class=tur")+1:sisaldabnime.index("</a></td><td>&nbsp;g")]

info = tekst.index(nimi) + 53 + len(nimi)  
elo = tekst[info:info+4]

i = 9266
asukoht = 0

while i < algus:
    i += 225
    asukoht += 1
    
nimi = nimi.replace(",", "")
nimejärjend = nimi.split()
täisnimi = ""
for nimi in reversed(nimejärjend):
    if nimejärjend.index(nimi) == 0:
        täisnimi += nimi
    else:
        täisnimi += nimi + " "

infojärjend = ['Mängija nimi (eesnimi- ja perekonnanimi): ' + täisnimi]
infojärjend.append('Elo reiting: ' + elo)
infojärjend.append('Asukoht FIDE top 100 mängijate edetabelis: ' + str(asukoht) + '. kohal')
for i in infojärjend:
    print(i)

valikud = ["Nime järgi", "Edetabeli asukoha järgi (100 piires)"]
valikubox = buttonbox("Valige, mille järgi otsite mängija kohta infot", image="malem2ngija.gif", choices=valikud)
if valikubox == "Nime järgi":
    #siin on otsimine nime järgi
    print("xqc")
else:
    #otsimine asukoha järgi
    print("doc")