# Másodfokú egyenlet megoldása Python program
# Developed by Dr. Gabor FACSKO (facskog@gamma.ttk.pte.hu)
# University of Pecs, Faculty of Science, Pecs, Hungary, 2024
# ------------------------------------------------------------
#
import math as m


# A determináns kiszámítása
def determinans(a,b,c):
    return (m.pow(b,2)-4*a*c)

# A gyökök kiszámítása
def gyokok (a,b,d):
    if (d>0):
        x1 = (-b-m.sqrt(d))/(2*a)
        x2 = (-b+m.sqrt(d))/(2*a)
        return ([x1,x2])
    if (d==0):
        x = -b/(2*a)
        return (x)
    if (d<0):
        '''
        x0 = -b/(2*a)
        x1 = m.sqrt(abs(d))/(2*a)
        x2 = m.sqrt(abs(d))/(2*a)
        return ([x0,x1,x2])
        '''
        return (-1)

# -----------------------------------------------------------------------------------------------------------------

# 3. Az ax2 + bx + c = 0 alakú másodfokú egyelet megoldása az (x ∈ R) valós számok halmazán, ahol a, b, c ∈ Z.
#
# (a) Vegyen fel tetszőleges egész a, b és c változót! Írja ki ax2 + bx + c = 0 alapban!

a = 1
b = 2
c = 0

print (str(a) + "x^2+"+str(b)+"x+"+str(c)+"=0")

# A determináns értéke
d=determinans(a,b,c)

# Az egyenlet megoldása
x=gyokok(a,b,d)


if (d>0):
    print ("Az egyenletnek két valós gyöke van.")
    print ("Az egyenlet gyökei: x1=" + str(x[0]) + " és x2=" + str(x[1]))

if (d==0):
    print ("Az egyenletnek egy valós gyöke van.")
    print ("Az egyenlet gyöke: x=" + str(x))

if (d<0):
    '''
    print ("Az egyenletnek két complex gyöke van.")
    print ("Az egyenlet complex gyökei: x1=" + str(x[0]) + "-" + str(x[0]) + "i és x2=" +
           str(x[0]) + "+" + str(x[2]) + "i")
    '''
    print ("Az egyenletnek nincs megoldása a valós számok halmazán.")
