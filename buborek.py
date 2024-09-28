# Buborékrendezés Python program
# Developed by Dr. Gabor FACSKO (facskog@gamma.ttk.pte.hu)
# University of Pecs, Faculty of Science, Pecs, Hungary, 2024
# ------------------------------------------------------------
#
import random as rd

# ------------------------------------------------------------

def feltoltes(N,minN,maxN):
    a = []
    # A tömb feltöltése véletlen számokkal (minN és maxN közötti értékekkel)
    for i in range(N):
        a.append(rd.randint(minN,maxN))
    return(a)

# ------------------------------------------------------------


def buborekRendezes(a):
    for i in range(len(a)-1,1,-1):
        for j in range(0,i):
            if (a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]

    return (a)

# ------------------------------------------------------------

# Keressük meg a tömb maximális elemét és annak inmdexét.
# Az a tömb (lista)
# Minimális szám
minN = 0
# Maximális szám
maxN = 100
# A tömb feltöltése
N = 20 # Tömb elemeinek a száma
# A tömb (lista)
a=feltoltes(N,minN,maxN)

# -------------------------------------------------------------------------

# Kiírom a tömb elemeit
print("A tömb elemei:",a)

# -------------------------------------------------------------------------

# Meghívom a buborék rnedzést
a = buborekRendezes(a)

# -------------------------------------------------------------------------

# Kiírom az eredményt
print("A tömb maximális eleme és annak indexe: ", a)
