# Megszamlalas Python program
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

# Eldönti, hogy bizonyos tulajdonságú elem szerepel-e a sorozatban
def megszamlalas(a,b):
    # Kiválasztja
    result = 0
    # Ciklus
    for e in a:
        if (e == b):
            result+=1

    return (result)

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
print("Hányszor szerepel a tömbben a 42-es szám? ", megszamlalas(a,42))
