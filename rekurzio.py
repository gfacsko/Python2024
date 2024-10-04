# Példák rekurzióra Pythonban
# Developed by Dr. Gabor FACSKO (facskog@gamma.ttk.pte.hu)
# University of Pecs, Faculty of Science, Pecs, Hungary, 2024
# ------------------------------------------------------------
#


# A rekurzív függvény meghívja saját magát
'''
# Faktoriális számítás
def faktor(n):
    if (n>1):
        return n*faktor(n-1)
    if (n==1):
        return (1)

print ("500!= ", faktor(500))
'''

# Fibonacci számok
def fibonacci(n):
    if (n==0):
        return 0;
    if (n==1):
        return 1;
    if (n>1):
        return (fibonacci(n-1)+fibonacci(n-2))

for f in range(20):
    print("Fibonacci számok: ", f, " ",fibonacci(f))
