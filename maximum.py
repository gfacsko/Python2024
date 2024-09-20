# Maximumkeresés Python program
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

def maximumKereses(a):
    # Az összeg
    maxV = a[0]
    maxI = 0
    # Kereső ciklus
    i = 0
    while (i < len(a)):
        if (a[i] > maxV):
            maxV = a[i]
            maxI = i
        i += 1

    return ([maxI,maxV])

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

# Kiírom az erdényt
print("A tömb maximális eleme és annak indexe: ", maximumKereses(a))
