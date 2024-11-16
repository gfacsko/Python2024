#
# guiTest GUI tesztprogram
# Developed by Dr. Gabor FACSKO, PhD (facskog@gamma.ttk.pte.hu)
# University of Pecsw, Faculty of Sciences,
# Institute of Matematics and Informatics, Pecs, 2024
# ------------------------------------------------------------------------
#
import tkinter as tk

# Az Exit gomb lenyomását kezelő függvény
def handle_click_exit(event):
    print("Az Exit gombot lenyomták.")
    exit(0)

# Az = gomb lenyomását kezelő függvény
def handle_click_egyen(event):
    print("A = gombot lenyomták.")
    greeting.configure(text="=")

# Az + gomb lenyomását kezelő függvény
def handle_click_add(event):
    print("A + gombot lenyomták.")
    greeting.configure(text="+")

# A * gomb lenyomását kezelő függvény
def handle_click_multi(event):
    print("A * gombot lenyomták.")
    greeting.configure(text="*")

# Az 1 gomb lenyomását kezelő függvény
def handle_click_egy(event):
    print("Az 1 gombot lenyomták.")
    greeting.configure(text="1")

# A 2 gomb lenyomását kezelő függvény
def handle_click_ketto(event):
    print("A 2 gombot lenyomták.")
    greeting.configure(text="2")

# Az 3 gomb lenyomását kezelő függvény
def handle_click_harom(event):
    print("A 3 gombot lenyomták.")
    greeting.configure(text="3")

# A 4 gomb lenyomását kezelő függvény
def handle_click_negy(event):
    print("A 4 gombot lenyomták.")
    greeting.configure(text="4")

# Az 5 gomb lenyomását kezelő függvény
def handle_click_ot(event):
    print("Az 5 gombot lenyomták.")
    greeting.configure(text="5")

# A 6 gomb lenyomását kezelő függvény
def handle_click_hat(event):
    print("A 6 gombot lenyomták.")
    greeting.configure(text="6")

# Az 7 gomb lenyomását kezelő függvény
def handle_click_het(event):
    print("A 7 gombot lenyomták.")
    greeting.configure(text="7")

# A 8 gomb lenyomását kezelő függvény
def handle_click_nyolc(event):
    print("A 8 gombot lenyomták.")
    greeting.configure(text="8")

# A 9 gomb lenyomását kezelő függvény
def handle_click_kilenc(event):
    print("A 9 gombot lenyomták.")
    greeting.configure(text="9")

# A 0 gomb lenyomását kezelő függvény
def handle_click_nulla(event):
    print("A 0 gombot lenyomták.")
    greeting.configure(text="0")

# Az ablak szélessége és magassága
width = 400
height = 600

# Létrehozza az ablakot
window = tk.Tk()

# Lekérdezi a képernyő méretei
scWidth = window.winfo_screenwidth()
scHeight = window.winfo_screenheight()

# Kiszámítja, hogy hol legyen az ablak, hol lesz a képernyő közepén
winX = (scWidth/2) - (width/2)
winY = (scHeight/2) - (height/2)

# Ez a függvény beállítja az ablak méretét és a helyzetét
window.geometry('%dx%d+%d+%d' % (width, height, winX, winY))

# Ez megadja az ablak címét
window.title("Első ablakos alkalmazás: számológép")
# Fehér háttér
window.configure(bg="white")

# Ezt már nem használjuk
#window.geometry("800x600")

# Kirak egy címkét (szöveget) az ablakba
greeting = tk.Label(text="Első GUI-m")
# Fehér háttér, fekete szöveg
greeting.configure(fg="black",bg="white")
# Ez rakja ki az ablakba a szöveget
greeting.pack()
# A gomb helyzete
greeting.place(x=100,y=50)

# Hozzáadja az + gombot
addGomb = tk.Button(text="+")
# Figyeli, hogy lenyomja-e valaki a + gombot
addGomb.bind("<Button-1>", handle_click_add)
# Ez rakja ki a gombot
addGomb.pack()
# A gomb helyzete
addGomb.place(x=50,y=500)

# Hozzáadja az 1 gombot
egyGomb = tk.Button(text="1")
# Figyeli, hogy lenyomja-e valaki a 1 gombot
egyGomb.bind("<Button-1>", handle_click_egy)
# Ez rakja ki a gombot
egyGomb.pack()
# A gomb helyzete
egyGomb.place(x=50,y=200)

# Hozzáadja a 2 gombot
kettoGomb = tk.Button(text="2")
# Figyeli, hogy lenyomja-e valaki a 2 gombot
kettoGomb.bind("<Button-1>", handle_click_ketto)
# Ez rakja ki a gombot
kettoGomb.pack()
# A gomb helyzete
kettoGomb.place(x=100,y=200)

# Hozzáadja a 3 gombot
haromGomb = tk.Button(text="3")
# Figyeli, hogy lenyomja-e valaki a 3 gombot
haromGomb.bind("<Button-1>", handle_click_harom)
# Ez rakja ki a gombot
haromGomb.pack()
# A gomb helyzete
haromGomb.place(x=150,y=200)

# Hozzáadja a 4 gombot
negyGomb = tk.Button(text="4")
# Figyeli, hogy lenyomja-e valaki a 4 gombot
negyGomb.bind("<Button-1>", handle_click_negy)
# Ez rakja ki a gombot
negyGomb.pack()
# A gomb helyzete
negyGomb.place(x=200,y=200)

# Hozzáadja az 5 gombot
otGomb = tk.Button(text="5")
# Figyeli, hogy lenyomja-e valaki az 5 gombot
otGomb.bind("<Button-1>", handle_click_ot)
# Ez rakja ki a gombot
otGomb.pack()
# A gomb helyzete
otGomb.place(x=50,y=250)

# Hozzáadja a 6 gombot
hatGomb = tk.Button(text="6")
# Figyeli, hogy lenyomja-e valaki a 6 gombot
hatGomb.bind("<Button-1>", handle_click_hat)
# Ez rakja ki a gombot
hatGomb.pack()
# A gomb helyzete
hatGomb.place(x=100,y=250)

# Hozzáadja a 7 gombot
hetGomb = tk.Button(text="7")
# Figyeli, hogy lenyomja-e valaki a 7 gombot
hetGomb.bind("<Button-1>", handle_click_het)
# Ez rakja ki a gombot
hetGomb.pack()
# A gomb helyzete
hetGomb.place(x=150,y=250)

# Hozzáadja a 8 gombot
nyolcGomb = tk.Button(text="8")
# Figyeli, hogy lenyomja-e valaki a 4 gombot
nyolcGomb.bind("<Button-1>", handle_click_nyolc)
# Ez rakja ki a gombot
nyolcGomb.pack()
# A gomb helyzete
nyolcGomb.place(x=200,y=250)

# Hozzáadja a 9 gombot
kilencGomb = tk.Button(text="9")
# Figyeli, hogy lenyomja-e valaki a 9 gombot
kilencGomb.bind("<Button-1>", handle_click_kilenc)
# Ez rakja ki a gombot
kilencGomb.pack()
# A gomb helyzete
kilencGomb.place(x=50,y=300)

# Hozzáadja a 0 gombot
nullaGomb = tk.Button(text="0")
# Figyeli, hogy lenyomja-e valaki a 0 gombot
nullaGomb.bind("<Button-1>", handle_click_nulla)
# Ez rakja ki a gombot
nullaGomb.pack()
# A gomb helyzete
nullaGomb.place(x=100,y=300)


# Hozzáadja az * gombot
multiGomb = tk.Button(text="*")
# Figyeli, hogy lenyomja-e valaki a * gombot
multiGomb.bind("<Button-1>", handle_click_multi)
# Ez rakja ki a gombot
multiGomb.pack()
# A gomb helyzete
multiGomb.place(x=100,y=500)

# Hozzáadja az = gombot
egyenGomb = tk.Button(text="=")
# Figyeli, hogy lenyomja-e valaki az egyenlőség gombot
egyenGomb.bind("<Button-1>", handle_click_egyen)
# Ez rakja ki a gombot
egyenGomb.pack()
# A gomb helyzete
egyenGomb.place(x=150,y=500)

# Hozzáad egy Exit gombot
exitGomb = tk.Button(text="Exit")
# Figyeli, hogy lenyomja-e valaki a bal egér gombot
exitGomb.bind("<Button-1>", handle_click_exit)
# Ez rakja ki a gombot
exitGomb.pack()
# A gomb helyzete
exitGomb.place(x=200,y=500)

# Ez egy ciklus indít, ami figyeli, hogy mi történik az ablakkal
window.mainloop()
