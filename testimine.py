from easygui import *
valikud = ["Nime järgi", "Edetabeli asukoha järgi (100 piires)"]
valikubox = buttonbox("Valige, mille järgi otsite mängija kohta infot", image="malem2ngija.gif", choices=valikud)
if valikubox == "Nime järgi":
    #siin on otsimine nime järgi
    print("xqc")
else:
    print("doc")