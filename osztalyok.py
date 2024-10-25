# Példaprogramok osztályokra Pythonban
# Developed by Dr. Gabor FACSKO (facskog@gamma.ttk.pte.hu)
# University of Pecs, Faculty of Science, Pecs, Hungary, 2024
# --

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
        return (self._Egyetem)

    def setEloadas(self,eloadas):
        self._eloadas=eloadas

    def getEloadas(self):
        return (self._Eloadas)

    def kiir(self):
        print("A Hallgató osztály parameterei:")
        print("Név: ",self._nev)
        print("Testsúly: ",self._testsuly)
        print("Magasság: ",self._magassag)
        print("Születési év: ",self._szuletesiEv)
        print("Születési hely: ",self._szuletesiHely)
        print("Egyetem: ",self._egyetem)
        print("Előadás: ",self._eloadas)

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

tamas = Hallgato()
print(tamas)

tamas.kiir()
