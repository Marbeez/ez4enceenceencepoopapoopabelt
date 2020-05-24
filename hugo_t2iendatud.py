from urllib.request import urlopen
from easygui import *

def otsitavmängija (otsitav):
    tekstarray = []
    
    algus = tekst.index(otsitav)

    temp_algus = algus + 53 + len(otsitav)  
    elo = tekst[temp_algus:temp_algus+4]
    tekstarray.append("Mängija ELO on: " + str(elo))
    
    i = 9266
    rank = 0

    while i < algus:
        i += 225
        rank += 1
    tekstarray.append("Mängija koht edetabelis on: " + str(rank))
    return tekstarray

edetabel = urlopen("https://ratings.fide.com/top.phtml?list=men")
baidid = edetabel.read()
tekst = baidid.decode()

msgbox("Tere tulemast programmi, mis otsib üles malemängija ELO edetabelist FIDE veebisaidil!")
nimearr = ["Eesnimi", "Perekonnanimi"]
nimed = multenterbox("Sisestage mängija ees- ja perekonnanimi", "Mängija otsija 3000", nimearr)

otsitav = nimed[1].title() + ", " + nimed[0].title()

infotekst = ""
i = 1

for line in otsitavmängija(otsitav):
    if len(otsitavmängija(otsitav)) == i:
        infotekst += line
    else :
        infotekst += line + "\n"
        i += 1

msgbox(infotekst)

#easygui täiendatud infot lisaks kursusematerjalile saime siit: http://easygui.sourceforge.net/tutorial.html
