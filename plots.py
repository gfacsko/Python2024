# Ábrázolás Python programok
# Developed by Dr. Gabor FACSKO (facskog@gamma.ttk.pte.hu)
# University of Pecs, Faculty of Science, Pecs, Hungary, 2024
# ------------------------------------------------------------
#
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(100)#[2,3,5,7,11,13,17,19]
y=np.pow(x,2)
print(y)

plt.plot(x,y)
plt.show()
