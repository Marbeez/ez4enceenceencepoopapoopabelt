from urllib.request import urlopen
edetabel = urlopen("https://ratings.fide.com/top.phtml?list=men")
baidid = edetabel.read()
tekst = [baidid.decode()]

def otsib():
    a = 0
    while (str(tekst)[0+a:i+a] == kogu_array) == False:
        a += 1
    print("aha")

kogu_array = []

eesnimi = str(input("Sisestage malemängja eesnimi: ")).title()
perenimi = str(input("Sisestage malemängja perekonnanimi: ")).title()

kogu_array.append(perenimi + ", " + eesnimi)
for i in kogu_array:
    i = len(i)

kogu_array = str(kogu_array)[2:-2]

otsib()