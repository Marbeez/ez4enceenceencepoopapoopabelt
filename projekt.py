# Laseb kasutada siin moodulis teises moodulis olevat koodi; siin programmis on vaja veebisaite käsitlevat moodulit ja graafilise kasutajaliidese moodulit
from urllib.request import urlopen
from easygui import *

# Programm avab veebisaidi, kust saab kätte infot mängijate kohta
edetabel = urlopen("https://ratings.fide.com/top.phtml?list=men")

# Muudab veebisaidi HTML-koodi pikaks string-objektiks
baidid = edetabel.read()
tekst = baidid.decode()

# Tekitab graafilise kasutajaliidese, kust saab valida, kas otsida malemängijat tema nime või edetabeli asukoha järgi
valikud = ["Nime järgi", "Edetabeli asukoha järgi (100 piires)"]
valikubox = buttonbox("Valige, mille järgi otsite mängija kohta infot", image="malem2ngija.gif", choices=valikud)

# Kood käivitub, kui valida nime järgi otsingu
if valikubox == "Nime järgi":
    
    # Funktsioon, mis tagastab string-objekti, mis sisaldab mängija kohta infot
    def otsitavmängija (otsitav):
        
        # Leiab mängija nime asukoha pikast HTML-koodist, mille läheduses on ka ülejäänud mängija info
        algus = tekst.index(otsitav)

        # 'algus' string-objekti ja veebisaidi ülesehituse kaudu leiab HTML-koodist ülejäänud mängija info (pikkused/infokildude asukohad tekstis leidis käsitsi)
        info = algus + 53 + len(otsitav)  
        elo = tekst[info:info+4]
        m2ngud = tekst[info+19:info+24]
        m2ngud = m2ngud.replace("<", "").replace("/", "").replace("t", "").replace("d", "")
        synniaasta = tekst[info+35:info+39]
        riik = tekst[info-18:info-15]
        
        # Pöörab antud nime ümber, et nimi oleks 'ees- ja perekonnanimi' formaadis
        otsitav = otsitav.replace(",", ":")
        nimejärjend = otsitav.split(":")
        täisnimi = ""
        for nimi in reversed(nimejärjend):
            if nimejärjend.index(nimi) == 0:
                täisnimi += nimi
            else:
                täisnimi += nimi + " "
        
        # Leiab veebisaidi ülesehituse järgi mängija edetabeli asukoha
        i = 9266
        asukoht = 0
        while i < algus:
            i += 225
            asukoht += 1
        
        # Lisab info järjendisse
        infojärjend = ['Mängija nimi (ees- ja perekonnanimi): ' + täisnimi]
        infojärjend.append('Elo reiting: ' + elo)
        infojärjend.append('Asukoht FIDE top 100 mängijate edetabelis: ' + str(asukoht) + '. kohal')
        infojärjend.append('Mängija mängis ' + str(m2ngud) + ' mängu see kuu')
        infojärjend.append('Mängija sündis ' + str(synniaasta) + '. aastal')
        infojärjend.append('Mängija on ' + str(riik) + ' riigi esindaja')
        
        # Võtab mängija infot sisaldavad string-objektid järjendist ning paneb need kõik ühte string-objekti kokku
        koguinfo = ""
        i = 0
        for line in infojärjend:
            if len(infojärjend) == i:
                koguinfo += line
            else :
                koguinfo += line + "\n"
                
        # Tagastab mängija kohta infot sisaldava string-objekti
        return koguinfo

    # Tekitab graafilise kasutajaliidese, kus kasutaja saab sisestada mängija nime programmi
    nimearr = ["Eesnimi", "Perekonnanimi"]
    nimed = multenterbox("Sisestage mängija ees- ja perekonnanimi", "Mängija otsija 3000", nimearr)
    
    # Tekitab graafilise kasutajaliidese, mis sisaldab antud mängija kohta infot, kasutades info leidmiseks funktsiooni otsitavmängija()
    msgbox(otsitavmängija(nimed[1].title() + ", " + nimed[0].title()))

# Kood käivitub, kui valida edetabeli asukoha järgi otsingu
else:
    
    # Funktsioon, mis tagastab string-objekti, mis sisaldab mängija kohta infot.
    def otsitavmängija (asukoht):
        
        # Leiab mängija edetabeli asukoha asukoha pikast HTML-koodist, mille läheduses on ka ülejäänud mängija info
        otsitav = "<td width=10>&nbsp;" + asukoht + "</a></td>"
        algus = tekst.index(otsitav)

        # 'algus' string-objekti ja veebisaidi ülesehituse kaudu leiab HTML-koodist üles antud mängija nime ja ülejäänud info
        sisaldabnime = tekst[algus:algus+200]
        nimi = sisaldabnime[sisaldabnime.index("class=tur")+len("class=tur")+1:sisaldabnime.index("</a></td><td>&nbsp;g")]
        info = tekst.index(nimi) + 53 + len(nimi)  
        elo = tekst[info:info+4]
        m2ngud = tekst[info+19:info+24]
        m2ngud = m2ngud.replace("<", "").replace("/", "").replace("t", "").replace("d", "")
        synniaasta = tekst[info+35:info+39]
        riik = tekst[info-18:info-15]
     
        # Pöörab antud nime ümber, et nimi oleks 'ees- ja perekonnanimi' formaadis
        nimi = nimi.replace(",", ":")
        nimejärjend = nimi.split(":")
        täisnimi = ""
        for nimi in reversed(nimejärjend):
            if nimejärjend.index(nimi) == 0:
                täisnimi += nimi
            else:
                täisnimi += nimi + " "

        # Lisab info järjendisse
        infojärjend = ['Mängija nimi (ees- ja perekonnanimi): ' + täisnimi]
        infojärjend.append('Elo reiting: ' + elo)
        infojärjend.append('Asukoht FIDE top 100 mängijate edetabelis: ' + str(asukoht) + '. kohal')
        infojärjend.append('Mängija mängis ' + str(m2ngud) + ' mängu see kuu')
        infojärjend.append('Mängija sündis ' + str(synniaasta) + '. aastal')
        infojärjend.append('Mängija on ' + str(riik) + ' riigi esindaja')
        
        # Võtab mängija infot sisaldavad string-objektid järjendist ning paneb need kõik ühte string-objekti kokku
        koguinfo = ""
        i = 0
        for line in infojärjend:
            if len(infojärjend) == i:
                koguinfo += line
            else :
                koguinfo += line + "\n"
                
        # Tagastab mängija kohta infot sisaldava string-objekti
        return koguinfo
    
    # Tekitab graafilise kasutajaliidese, kus kasutaja saab sisestada mängija edetabeli asukoha programmi
    asukohtgui = enterbox("Sisestage malemängja asukoht edetabelis", "Mängija otsija 3000")

    # Tekitab graafilise kasutajaliidese, mis sisaldab antud mängija kohta infot, kasutades info leidmiseks funktsiooni otsitavmängija()
    msgbox(otsitavmängija(asukohtgui))