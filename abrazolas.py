# Ábrázolás Python programok
# Developed by Dr. Gabor FACSKO (facskog@gamma.ttk.pte.hu)
# University of Pecs, Faculty of Science, Pecs, Hungary, 2024
# ------------------------------------------------------------
#
import matplotlib.pyplot as plt
import numpy as np

'''
x=np.arange(200)-100.0
fx=np.pow(x,2)
gx=np.pow(x,3)
hx=np.pow(x,4)

# Első ábra ---------------------------------------------------------------------------------------------------
plt.subplot(2,2,1)

# Több függvény ábrázolása
plt.plot(x,fx,color='k',linestyle='-',label='$f(x)=x^2$') #,linewidth=1
plt.plot(x,gx,color='g',linestyle='--',label='$g(x)=x^3$')
plt.plot(x,hx,color='r',linestyle=':',label='$h(x)=x^4$')
# Tengely intervalumok
plt.xlim([-100,100])
plt.ylim([-10000,10000])
# Cím
plt.title("Függvények",fontsize=20)
# Tengely feliratok betűmérete
plt.xlabel("x",fontsize=20)
plt.ylabel("y",fontsize=20)
# Címkék betűmérete
plt.tick_params(axis='both', which='major', labelsize=15)

# Kiírja a magyarázatot
#plt.legend()


# Második ábra ---------------------------------------------------------------------------------------------------
plt.subplot(2,2,2)

y=x/100*np.pi
ky=np.sin(y)
ly=np.cos(y)

plt.plot(y,ky,color='b',linestyle='-',label='$k(y)=\sin(y)$') #,linewidth=1
plt.plot(y,ly,color='c',linestyle='-',label='$l(y)=\cos(y)$')
# Tengely intervalumok
plt.xlim([-np.pi,np.pi])
plt.ylim([-1,1])
# Cím
plt.title("Trigonometriai függvények",fontsize=20)
# Tengely feliratok betűmérete
plt.xlabel("x",fontsize=20)
plt.ylabel("y",fontsize=20)
# Címkék betűmérete
plt.tick_params(axis='both', which='major', labelsize=15)
# Az x tengely címkéi
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],['$-\pi$','-$\pi$/2','0','$\pi$/2','$\pi$'],rotation=0)

# Harmadik ábra ---------------------------------------------------------------------------------------------------
plt.subplot(2,2,3)

# Szórás diagram, független értékek
plt.scatter(x,fx,s=x,c=gx,alpha=0.5,label='Pöttyök')
# A tengelyek hossza
plt.xlim([0,100])
plt.ylim([0,10000])
# Az ábra címe és a tengelyek feliratai
plt.title('Színes pöttyök',fontsize=20)
# Tengely feliratok betűmérete
plt.xlabel("x",fontsize=20)
plt.ylabel("f(x)",fontsize=20)
# Címkék betűmérete
plt.tick_params(axis='both', which='major', labelsize=15)

# Negyedik ábra ---------------------------------------------------------------------------------------------------
plt.subplot(2,2,4)

#plt.hist(fx,bins=10,histtype='step',stacked=True, fill=False,color='Black',label='Lépcsők')
plt.xlim([0,5000])
plt.ylim([0,100])

# Az ábra címe és a tengelyek feliratai
plt.title('Histogram',fontsize=20)
# Tengely feliratok betűmérete
plt.xlabel("f(x)",fontsize=20)
plt.ylabel("Arány [%]",fontsize=20)
# Címkék betűmérete
plt.tick_params(axis='both', which='major', labelsize=15)

# ----------------------------------------------------------------------------------------------------

# Minden ábra magyarázata egyben
plt.figlegend()

# Megjelenik az ábra
plt.show()
'''

'''
szavak=['a','az','és','de','izé','igen','nem']
szavakSzama=[100,90,50,70,200,60,10]

# Barplot
#plt.bar(szavak,szavakSzama,color='k',label='Barplot')
plt.bar(szavak,np.multiply(szavakSzama/np.sum(szavakSzama),100),color='k',label='Barplot')

# Határok
#plt.xlim([0,5000]) # Értelmetlen
plt.ylim([0,100]) # Százalékra jó

# Az ábra címe és a tengelyek feliratai
plt.title('Bar plot',fontsize=20)
# Tengely feliratok betűmérete
plt.xlabel("Szavak",fontsize=20)
plt.ylabel("Szavak száma [%]",fontsize=20)
# Címkék betűmérete
plt.tick_params(axis='both', which='major', labelsize=15)
# Címkék forgatása az x tengelyen
plt.xticks(rotation=90)

# Minden ábra magyarázata egyben
plt.figlegend()

plt.show()
'''

'''
# Contour plot készítése

# Adatgenerálás
x, y = np.meshgrid(np.arange(7), np.arange(3,10))
z = np.sin(0.5 * x) * np.cos(0.52 * y)

# Ábrázolás
cs = plt.contourf(x, y, z)
plt.contour(cs, colors='k')
plt.title("Contour plot")

# Háló
plt.grid(c='k', ls='-', alpha=0.3)

plt.show()
'''
# Extra könyvtárak
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data


# Ábrázolás 3D-ben

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))/np.sqrt(x ** 2 + y ** 2)


x = np.linspace(-60, 60, 300)
y = np.linspace(-60, 60, 300)
X, Y = np.meshgrid(x, y)
Z = f(X,Y)

'''
# Előkészítés
#ax = plt.axes(projection='3d')
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='rainbow') # binary
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');
# 3D ábra
#ax.plot3D(X, Y, Z) # , 'k.'
'''

#x=np.arange(200)-100.0
#y=x/10*np.pi

#z=f(y,y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(X,Y,Z)

# Ábra kirajzolása
plt.show()
