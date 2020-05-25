from urllib.request import urlopen
from easygui import *

edetabel = urlopen("https://ratings.fide.com/top.phtml?list=men")
baidid = edetabel.read()
tekst = baidid.decode()

valikud = ["Nime järgi", "Edetabeli asukoha järgi (100 piires)"]
valikubox = buttonbox("Valige, mille järgi otsite mängija kohta infot", image="malem2ngija.gif", choices=valikud)
if valikubox == "Nime järgi":
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

else:
    asukohtgui = enterbox("Sisestage malemängja asukoht edetabelis", "Mängija otsija 3000")
    asukoht = asukohtgui.title()

    otsitav = "<td width=10>&nbsp;" + asukoht + "</a></td>"
    algus = tekst.index(otsitav)

    sisaldabnime = tekst[algus:algus+200]
    nimi = sisaldabnime[sisaldabnime.index("class=tur")+len("class=tur")+1:sisaldabnime.index("</a></td><td>&nbsp;g")]

    info = tekst.index(nimi) + 53 + len(nimi)  
    elo = tekst[info:info+4]
    m2ngud = tekst[info+19:info+24]
    m2ngud = m2ngud.replace("<", "").replace("/", "").replace("t", "").replace("d", "")
    synniaasta = tekst[info+35:info+39]
    riik = tekst[info-18:info-15]

    i = 9266
    asukoht = 0

    while i < algus:
        i += 225
        asukoht += 1
        
    nimi = nimi.replace(",", ":")
    nimejärjend = nimi.split(":")
    täisnimi = ""
    for nimi in reversed(nimejärjend):
        if nimejärjend.index(nimi) == 0:
            täisnimi += nimi
        else:
            täisnimi += nimi + " "

    infojärjend = ['Mängija nimi (ees- ja perekonnanimi): ' + täisnimi]
    infojärjend.append('Elo reiting: ' + elo)
    infojärjend.append('Asukoht FIDE top 100 mängijate edetabelis: ' + str(asukoht) + '. kohal')
    infojärjend.append('Mängija mängis ' + str(m2ngud) + ' mängu see kuu')
    infojärjend.append('Mängija sündis ' + str(synniaasta) + ' aastal')
    infojärjend.append('Mängija on ' + str(riik) + ' riigi esindaja')
    koguinfo = ""
    i = 0
    for line in infojärjend:
        if len(infojärjend) == i:
            koguinfo += line
        else :
            koguinfo += line + "\n"
    
    msgbox(koguinfo)
