import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons, CheckButtons
from matplotlib import animation
from random import *



##################################   Marche Aléatoire      ####################################


def marche(npas):
    x=0
    for i in range(npas):
        if (random()>0.5):
            x = x+1
        else:
            x = x-1
    return(x)

def Simutotale(Nmarcheur,npas):
    positions=[0]*Nmarcheur
    for i in range(Nmarcheur):
        positions[i]=marche(npas)
    return(positions)
    
Nmarcheur_0=500
npas_0 = 1
num_bins=50

resultats = Simutotale(Nmarcheur_0,npas_0)

# Creation de la figure
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.22, bottom=0.15)

ax.set_xlabel('Position')
ax.set_ylabel('Probabilité de présence')
ax.set_title('Marche aléatoire et diffusion')

# Limites
xmin=-150
xmax=150
ymin=0.0
ymax=0.05
# Specification des limites des axes (xmin,xmax,ymin,ymax)
plt.axis([xmin,xmax,ymin,ymax])

x=np.linspace(xmin,xmax,num=1001)

    
histo = ax.hist(resultats, num_bins, density=1)
gaussienne = ax.plot(x,np.exp(-x**2/(2*npas_0))/np.sqrt(npas_0*2*np.pi))

# Creation de la barre pour modifier npas
axn = plt.axes([0.22, 0.03, 0.68, 0.03])
sn = Slider(axn, 'Nombre de pas', 1, 10000, valinit=npas_0)

# Fonction de mise a jour du graphique
def update(val):
    ncur = math.floor(sn.val) # On recupere la valeur de la barre sn comme nouveau nombre de pas
    resultcur = Simutotale(Nmarcheur_0,ncur)
    ax.cla()
    ax.axis([xmin,xmax,ymin,ymax])
    ax.set_xlabel('Position')
    ax.set_ylabel('Probabilité de présence')
    ax.set_title('Marche aléatoire et diffusion')
    histo = ax.hist(resultcur, num_bins, density=1)
    gaussienne = ax.plot(x,np.exp(-x**2/(2*ncur))/np.sqrt(ncur*2*np.pi))
    fig.canvas.draw_idle()


sn.on_changed(update) # lorsque la barre sn est modifiee, on applique la fonction update




