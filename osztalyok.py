# Példaprogramok osztályokra Pythonban
# Developed by Dr. Gabor FACSKO (facskog@gamma.ttk.pte.hu)
# University of Pecs, Faculty of Science, Pecs, Hungary, 2024
# --

import numpy as np

# Elso osztályom
class Ember: #(object):
    def __init__(self,nev="John Doe",testsuly=120,magassag=186,szuletesiEv=1975,szuletesiHely="Baja"):
        self._nev = nev
        self._testsuly=testsuly
        self._magassag=magassag
        self._szuletesiEv=szuletesiEv
        self._szuletesiHely=szuletesiHely

    def __str__(self):
        return (self._nev + " " + str(self._testsuly)  + " " + str(self._magassag) + " " +
                str(self._szuletesiEv) + " " + self._szuletesiHely)

    def setNev(self,nev):
        self._nev=nev

    def getNev(self):
        return (self._nev)

    def setTestsuly(self,testsuly):
        self._testsuly=testsuly

    def getTestsuly(self):
        return (self._testsuly)

    def setMagassag(self,magassag):
        self._magassag=magassag

    def getMagassag(self):
        return (self._magassag)

    def setSzuletesiEv(self,szuletesiEv):
        self._szuletesiEv=szuletesiEv

    def getSzuletesiEv(self):
        return (self._szuletesiEv)

    def setSzuletesiHely(self,szuletesiHely):
        self._szuletesiHely=szuletesiHely

    def getSzuletesiHely(self):
        return (self._szuletesiHely)

    @property
    def nev(self):
        return self._nev

    @nev.setter
    def nev(self, nev):
        self._nev = nev

    def kiir(self):
        print("Az Ember osztály parameterei:")
        print("Név: ",self._nev)
        print("Testsúly: ",self._testsuly)
        print("Magasság: ",self._magassag)
        print("Születési év: ",self._szuletesiEv)
        print("Születési hely: ",self._szuletesiHely)

# ---------------------------------------------------------------------------------------------------------

class Hallgato(Ember):
    def __init__(self,nev="John Doe",testsuly=120,magassag=186,szuletesiEv=1975,szuletesiHely="Baja",
                 egyetem="PTE",eloadas="Linalg"):
        self._nev = nev
        self._testsuly=testsuly
        self._magassag=magassag
        self._szuletesiEv=szuletesiEv
        self._szuletesiHely=szuletesiHely
        self._egyetem = egyetem
        self._eloadas = eloadas

    def __str__(self):
        return (self._nev + " " + str(self._testsuly)  + " " + str(self._magassag) + " " +
            str(self._szuletesiEv) + " " + self._szuletesiHely + " " + self._egyetem + " " +
                self._eloadas)

    def setEgyetem(self,egyetem):
        self._egyetem=egyetem

    def getEgyetem(self):
        return (self._egyetem)

    def setEloadas(self,eloadas):
        self._eloadas=eloadas

    def getEloadas(self):
        return (self._eloadas)

    def kiir(self):
        print("A Hallgató osztály paraméterei:")
        print("Név: ",self._nev)
        print("Testsúly: ",self._testsuly)
        print("Magasság: ",self._magassag)
        print("Születési év: ",self._szuletesiEv)
        print("Születési hely: ",self._szuletesiHely)
        print("Egyetem: ",self._egyetem)
        print("Előadás: ",self._eloadas)

# ---------------------------------------------------------------------------------------------------------

class Oktato(Ember):
    def __init__(self,nev="Oktató Edömér",testsuly=120,magassag=186,szuletesiEv=1975,szuletesiHely="Baja",
                 egyetem="PTE",eloadas="Linalg",beosztas="adjunktus",kurzus="Linalg",):
        self._nev = nev
        self._testsuly=testsuly
        self._magassag=magassag
        self._szuletesiEv=szuletesiEv
        self._szuletesiHely=szuletesiHely
        self._beosztas = beosztas
        self._kurzus = kurzus

    def __str__(self):
        return (self._nev + " " + str(self._testsuly)  + " " + str(self._magassag) + " " +
            str(self._szuletesiEv) + " " + self._szuletesiHely + " " + " " + self._beosztas + " " + self._kurzus)

    def setBeosztas(self,beosztas):
        self._beosztas=beosztas

    def getBeosztas(self):
        return (self._beosztas)

    def setKurzus(self,kurzus):
        self._kurzus=kurzus

    def getKurzus(self):
        return (self._kurzus)

    def kiir(self):
        print("Az Oktató osztály paraméterei:")
        print("Név: ",self._nev)
        print("Testsúly: ",self._testsuly)
        print("Magasság: ",self._magassag)
        print("Születési év: ",self._szuletesiEv)
        print("Születési hely: ",self._szuletesiHely)
        print("Beosztás: ",self._beosztas)
        print("Kurzus: ",self._kurzus)

# ---------------------------------------------------------------------------------------------------------

class Doktorandusz(Hallgato,Oktato):
    def __init__(self,nev="Tudálékos Annamária",testsuly=50,magassag=146,szuletesiEv=1995,szuletesiHely="Budapest",
                 egyetem="PTE",eloadas="Linalg",beosztas="Phd hallgató",kurzus="Linalg"):
        self._nev = nev
        self._testsuly=testsuly
        self._magassag=magassag
        self._szuletesiEv=szuletesiEv
        self._szuletesiHely=szuletesiHely
        self._beosztas = beosztas
        self._kurzus = kurzus
        self._egyetem = egyetem
        self._eloadas = eloadas

    def __str__(self):
        return (self._nev + " " + str(self._testsuly)  + " " + str(self._magassag) + " " +
            str(self._szuletesiEv) + " " + self._szuletesiHely + " " + " " + self._beosztas + " " +
                self._kurzus + " " + self._egyetem + " " + self._eloadas)

    def kiir(self):
        print("Az Oktató osztály paraméterei:")
        print("Név: ",self._nev)
        print("Testsúly: ",self._testsuly)
        print("Magasság: ",self._magassag)
        print("Születési év: ",self._szuletesiEv)
        print("Születési hely: ",self._szuletesiHely)
        print("Beosztás: ",self._beosztas)
        print("Kurzus: ",self._kurzus)
        print("Egyetem: ",self._egyetem)
        print("Előadás: ",self._eloadas)

# ---------------------------------------------------------------------------------------------------------

# Saját osztály, operátor overloadingra példák
class NegyesVektor:
    def __init__(self,x=0,y=0,z=0,w=0):
        self._x = x
        self._y = y
        self._z = z
        self._w = w

    def setX(self,x):
        self._x = x

    def getX(self):
        return(self._x)

    def setY(self,y):
        self._y = y

    def getY(self):
        return(self._y)

    def setZ(self,z):
        self._z = z

    def getZ(self):
        return(self._z)

    def setW(self,w):
        self._w = w

    def getW(self):
        return(self._w)

    # A négyesvektor hossza
    def length(self):
        return (np.sqrt(np.pow(self._x,2)+np.pow(self._y,2)+np.pow(self._z,2)+np.pow(self._w,2)))


    def __str__(self):
        return ("(" + str(self._x) + "," + str(self._y)  + "," + str(self._z) + "," + str(self._w) + ")")

    def __add__(self,v):
        if (isinstance(v,NegyesVektor)):
            return (NegyesVektor(self._x + v.getX(),
                             self._y + v.getY(),
                             self._z + v.getZ(),
                             self._w + v.getW()))

        return ("NegyesVektort csak NegyesVektorral lehet összeadni.")

    def __sub__(self,v):
        if (isinstance(v,NegyesVektor)):
            return (NegyesVektor(self._x - v.getX(),
                             self._y - v.getY(),
                             self._z - v.getZ(),
                             self._w - v.getW()))

        return ("NegyesVektort csak NegyesVektorból lehet kivonni.")

    def __mul__(self,v):
        if (isinstance(v,NegyesVektor)):
            return (self._x * v.getX() + self._y * v.getY() + self._z * v.getZ() + self._w * v.getW())

        return (NegyesVektor(self._x*v,self._y*v,self._z*v,self._w*v))

    def __truediv__(self, v):
        if (isinstance(v,NegyesVektor)):
            return ("Vektorokat nem lehet elosztani egymással.")

        return (NegyesVektor(self._x/v,self._y/v,self._z/v,self._w/v))

    def __eq__(self,v):
        return (self._x == v.getX() & self._y == v.getY() & self._z == v.getZ() & self._w == v.getW())

    def __ne__(self,v):
        return ((self._x != v.getX() | self._y != v.getY()) | self._z != v.getZ()  | self._w != v.getW())

    def __lt__(self, v):
        return (self.length()<v.length())

    def __gt__(self, v):
        return (self.length()>v.length())

    def __le__(self, v):
        return (self.length()<=v.length())

    def __ge__(self, v):
        return (self.length()>=v.length())

# ---------------------------------------------------------------------------------------------------------

#joe = Ember()
#jane = Ember("Jane Doe",50,160,2000,"DC")

#print(jane)
#print(joe)

#joe.kiir()
#jane.kiir()

#joe.nev="Joe Doe"
#print(joe.nev)

#jane.setNev("Agnes")
#jane.setSzuletesiEv(2010)
#jane._testsuly = 300
#jane.kiir()

#tamas = Hallgato()
#print(tamas)

#tamas.kiir()

#gabor=Oktato()
#print(gabor)

#gabor.kiir()

#amalia=Doktorandusz()
#amalia.kiir()

v1=NegyesVektor(1,1,1,1)
v2=NegyesVektor(2,2,2,2)

print("Az első négyesvektor:", v1)
print("A második negyesvektor: ", v2)

print(isinstance(v1, NegyesVektor))
print(isinstance(v1, Hallgato))
print(isinstance(v1.getX(),float))

print("A két négyesvektor összege:", v1+v2)
print("Egy négyesvektor és egy skalár összege: ", v1+1)
print("Egy négyesvektor és egy skalár különbsége: ", v1-1)
print("Egy négyesvektor és egy skalár szorzata: ", v1*7)
print("Egy négyesvektor és egy skalár hányadosa: ", v2/2)
print("Két vektor hányadosa:", v1/v2)

'''
print("A két négyesvektor különbsége:", v1-v2)
print("A két négyesvektor skaláris szorzata:", v1*v2)

print("v1 == v2: ", v1 == v2)
print("v1 == v1: ", v1 == v1)
print("v1 != v2: ", v1 != v2)
print("v1 != v1: ", v1 != v1)
#print("A v1 vektor hossza: ", v1.len())
print("v1<v2: ", v1<v2)
print("v2<v2: ", v2<v2)
print("v1>v2: ", v1>v2)
print("v2>v2: ", v2>v2)
print("v1<=v2: ", v1<=v2)
print("v2<=v2: ", v2<=v2)
print("v1=>v2: ", v1>=v2)
print("v2=>v2: ", v2>=v2)
'''

