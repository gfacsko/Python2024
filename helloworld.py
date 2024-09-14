# Első Python program
# Developed by Dr. Gabor FACSKO (facskog@gamma.ttk.pte.hu)
# University of Pecs, Faculty of Science, Pecs, Hungary, 2024
# ------------------------------------------------------------
#

'''
# Hello World
print("Hello")

# Alapvető típusok
i = 100

print(i)

print(type(i))

r = 2.71

print(r)

s = "137"

print(s)

print(type(float(s)))
print(type(int(s)))
print(type(str(r)))

# Elágazás
if (i==10):
    print(i)
else:
    print("Ez nem tíz")


# While ciklus
j=0
while(j<10):
    print(j)
    j+=1

# For ciklus
for j in range(100):
    print(j)

'''
# Listak
szamok = [9.3, 7.5, 3.7, 0.1, 4.2]

'''
print(szamok)
print(type(szamok))


print(szamok[3])

print(len(szamok))


i=0
while (i<len(szamok)):
    print(szamok[i])
    i+=1

for i in range(len(szamok)):
    print(szamok[i])

for sz in szamok:
    print(sz)

# Műveletek listákkal: hozzáfűzés
szamok.append(3.14)
szamok.append('valami')

print(szamok)

szamok.pop(-1)

print(szamok)

# Műveletek listákkal: rendezés
szamok.sort()

print(szamok)

# Műveletek listákkal: eltávolítás
szamok.pop(-2)

print(szamok)

for sz in szamok:
    print(sz)

# Értékcsere
a=1
b=2
a,b=b,a

print(a)
print(b)

# A range utasítás
for q in range(0,10,3):#range(-1,-10,-3)
    print(q)


print(range(5,10))
print(range(0,10,3))
print(range(-1,-10,-3))



# Ideiglenes másolat készítése (?)
print(szamok)
for s in szamok[:]:
    if (s < 4): szamok.remove(s)

print(szamok)

'''
# Python specifikus utasítás
print([i**2 for i in range(10)])


# Reverse
for i in reversed(range(0,4)):
  print(i)

