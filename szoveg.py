
# Szövegkezelés Python programok
# Developed by Dr. Gabor FACSKO (facskog@gamma.ttk.pte.hu)
# University of Pecs, Faculty of Science, Pecs, Hungary, 2024
# ------------------------------------------------------------
#
s = "Indul a görög aludni"

t = "görög"

print(s+" "+t)

print(t in s)

print(t * 3)

print(s[2])
print(type(s[2]))

print(s[8:13])
print(s[1:11:2])

print(t.capitalize())

print(s.count("ö"))

print(s.endswith("ni"))

print(s.find(t))

try:
    print(s.index("z"))
except:
    print("Hiba lépett fel")

print(' '.join(["alma","körte","szőlő"]))

print(s.partition(' '))

print(s.replace(t,'török'))
print(s.replace(' ','_'))

print(s.split(' '))

print(s.splitlines())

print(s.startswith("Indul"))
print(s.startswith(t))

print(s.title())

# Maximumkeresés Python program
# Developed by Dr. Gabor FACSKO (facskog@gamma.ttk.pte.hu)
# University of Pecs, Faculty of Science, Pecs, Hungary, 2024
# -----------------------------------------------------------
