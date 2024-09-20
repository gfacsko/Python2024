# Összegzés Python program
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

def osszegzes(a):
    # Az összeg
    s = 0#a[0]
    # Összegző ciklus
    #for i in range(1,len(a)):
    #    s = s + a[i]
    for szam in a:
        #s = s + szam
        s += szam
    return (s)

# ------------------------------------------------------------



# Összegezzük az tömb (lista) elemeit.
# Az a tömb (lista)
#a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 42, 137]
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
print("A tömb elemeinek összege: ", osszegzes(a))
