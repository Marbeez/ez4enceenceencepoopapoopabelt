from urllib.request import urlopen
edetabel = urlopen("https://ratings.fide.com/top.phtml?list=men")
baidid = edetabel.read()
tekst = [baidid.decode()]

def otsib():
    a = 0
    while (str(tekst)[9266+a : 9266+i+a] == kogu_array) == False:
        a += 1
    print("aha")

eesnimi = str(input("Sisestage malemängja eesnimi: ")).title()
perenimi = str(input("Sisestage malemängja perekonnanimi: ")).title()

kogu_array = [perenimi + ", " + eesnimi]

for i in kogu_array:
    i = len(i)

kogu_array = str(kogu_array)[2:-2]

otsib()