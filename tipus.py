# Egyszerű típusok Python program
# Developed by Dr. Gabor FACSKO (facskog@gamma.ttk.pte.hu)
# University of Pecs, Faculty of Science, Pecs, Hungary, 2024
# ------------------------------------------------------------
#

'''
# Példa hibakezelésekre
n=-1 # A változó kezdeti értéke
# Addig kér be adatot, amíg nem kapja meg, amit akar
while (n<=0):
    # Fejlett hibakezelés kivétel kezeléssel
    try:
        # Bekér egy egész számot promptról
        n=int(input("Adjon meg egy pozitív egészszámot: "))
        # Egyszerű hibakezelés if-fel
        if (n <= 0):
            print("Pozitív számot kellett volna beírnia.")
    # Ha nem integer számot adunk meg, akkor ezt a kivételt dobja
    except ValueError:
        print("A program csak pozitív egész számokat fogad el.")
    # Minden más esetre kék halál. :(
    except:
        print("Általános védelmi hiba")

# Kiírja a beírt pozitív egész számot
print("A beírt szám: ",n)
'''

'''
a=(2, 3, 5, 7, 11, 13, 17, 19, 'RRR')

print("A tuple értékei: ",a)
print("Egy elem száma: ", a.count(2))
print("Egy elem helye: ", a.index(7))
'''

'''
# Példák halmazokra
b=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(type(b))

b_tuple=tuple(b)
print(type(b_tuple))

h={2, 3, 5, 7, 11, 'aa', 'zz', 3.14}
print(h)

b_set=set(b)
print(b_set)

print("Halmazok metszete: ", h.intersection(b_set))
print("Halmazok uniója: ", h.union(b_set))

print("A halmaz tartalmazza-e ezt az elemet: ", ('b' in b_set))
'''

'''
# Példák szótárakra
sz={'egy':'yksi', 'ketto':'kaksi', 'harom':'kolme', 'negy':'nelja' }

# Kiírja a kulcshoz tarto értéket
print(sz['harom'])
print(sz.pop('ketto'))
# Kiírja az értékeket
print(sz.values())
# Kiírja a kulcsokat
print(sz.keys())
# Kiír mindent
print(sz.items())
'''

'''
no=None
print(no)
print(type(no))
'''

