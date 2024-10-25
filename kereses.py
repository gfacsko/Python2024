# Keresés Python program
# Developed by Dr. Gabor FACSKO (facskog@gamma.ttk.pte.hu)
# University of Pecs, Faculty of Science, Pecs, Hungary, 2024
# ------------------------------------------------------------
#
import random as rd

# ------------------------------------------------------------

def feltoltes(N,minV,maxV):
    a = []
    # A tömb feltöltése véletlen számokkal (minN és maxN közötti értékekkel)
    for i in range(N):
        a.append(rd.randint(minV,maxV))
    return(a)


# ------------------------------------------------------------

# Megkeres egy elemet és visszaadaja az indexét.
# Ha nincs a sorozatban, akkor -1-et ad vissza.
def kereses(a,b):
    # A keresett elem indexe
    iB = -1
    # Ciklus
    i=0 # Ciluis változó
    while (i<len(a)):
        if (a[i] == b):
            iB=i
            i=len(a) # Kiugrom a ciklusból

        i+=1

    return (iB)

# ------------------------------------------------------------

# Az a tömb (lista)
# Minimális szám
minV = 0
# Maximális szám
maxV = 100
# A tömb feltöltése
N = 20 # Tömb elemeinek a száma
# A tömb (lista)
a=feltoltes(N,minV,maxV)

# -------------------------------------------------------------------------

# Kiírom a tömb elemeit
print("A tömb elemei:",a)

# -------------------------------------------------------------------------

# Kiírom az eredményt
valasz="Nem."
iB = kereses(a,21) # Az iB a keresett elem indexe.
if (iB > -1):
    valasz="Igen, a(z) " + str(iB) + ". helyen"

print("Szerepel-e a 21 a listában? " + valasz)
