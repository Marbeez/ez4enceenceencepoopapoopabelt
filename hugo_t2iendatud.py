from urllib.request import urlopen
from easygui import *

edetabel = urlopen("https://ratings.fide.com/top.phtml?list=men")
baidid = edetabel.read()
tekst = baidid.decode()

msgbox("Tere tulemast programmi, mis otsib üles malemängija ELO edetabelist FIDE veebisaidil!")
nimearr = ["Eesnimi", "Perekonnanimi"]
nimed = multenterbox("Sisestage mängija ees- ja perekonnanimi", "Mängija otsija 3000", nimearr)

otsitav = nimed[1].title() + ", " + nimed[0].title()

algus = tekst.index(otsitav)

temp_algus = algus + 53 + len(otsitav)  
elo = tekst[temp_algus:temp_algus+4]

i = 9266
rank = 0

while i < algus:
    i += 225
    rank += 1
    
print(elo)
print(rank)
msgbox("Mängija ELO on: " + str(elo) + "\n" + "Mängija koht edetabelis on: " + str(rank))

#easygui täiendatud infot lisaks kursusematerjalile saime siit: http://easygui.sourceforge.net/tutorial.html