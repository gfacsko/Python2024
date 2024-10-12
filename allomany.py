# Állományok Python program
# Developed by Dr. Gabor FACSKO (facskog@gamma.ttk.pte.hu)
# University of Pecs, Faculty of Science, Pecs, Hungary, 2024
# ------------------------------------------------------------
#
import matplotlib.pyplot as plt

# Initialisation
workdir=""
datafile="angol.txt"#lorem.txt"

# Megnyitandó állomány neve
filename=workdir+datafile

# Állomány megnyitása
sourcefile = open(filename)
# Minden beolvasása
mindenSzo=[]
text = sourcefile.readlines()
for line in text:
    #print(line)
    szavak=line.strip().replace('.','').lower().split()
    mindenSzo.append(szavak)

mindenSzo=mindenSzo[0]

print(mindenSzo)

mindenSzo.sort()

mSz=set(mindenSzo)

mSz=mSz.intersection(mSz)

print(mSz)

egyediSzo=list(mSz)

egyediSzo.sort()

print(egyediSzo)

result=[]
for sz in egyediSzo:
    result.append(mindenSzo.count(sz))

plt.bar(egyediSzo,result)
plt.xticks(rotation=90)
plt.show()

'''
# Soronkénti beolvasás
line=sourcefile.readline()
# Amíg van mit beolvasni. 
while (line):
    print(line)
    line=sourcefile.readline()
'''
# Az állomány bezárása.
sourcefile.close()
