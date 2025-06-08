

import numpy as np
import matplotlib.pyplot as plt  
import csv
from scipy.integrate import quad   # Pour intégrer
from scipy.integrate import odeint # Pour la resolution d'equations differentielles



#########################################################################################################################
##########################         Différence T0 TBorda TExacte        ##################################################
#########################################################################################################################


L = 1     # longueur en m
g = 9.81  # acceleration pesanteur en m/s2
m = 0.1   # masse en kg

# Pulsation et période propre
omega_0 = np.sqrt(g/L)     # rad/s
T_0 = 2 * np.pi / omega_0  # s

# Choisir les theta et les transformer en radian
theta_0_deg = np.arange(0.,180.+1.,1.)
theta_0 = theta_0_deg * np.pi / 180.

# Periode de Borda
T_Borda = T_0 * (1. + (theta_0**2 / 16.))


# Fonction à intégrer pour la période exacte
def integrand(theta, k):
    return 1 / np.sqrt(1 - k**2 * np.sin(theta)**2)

# Calcul de la période exacte
x = np.sin(theta_0 / 2)
T_exact = np.zeros(len(theta_0),dtype=float)
for i in range(len(theta_0)) :
    Integ, _ = quad(integrand, 0, np.pi / 2, args=(x[i],))
    T_exact[i] = 4 * np.sqrt(L / g) * Integ     


# Chercher ecart de 1% entre T0 et T_Exacte
for i in range(len(theta_0)-1) :
    if np.abs(((T_exact[i] - T_0)  / T_exact[i]) - 0.01) <= 0.0005 :
        ilim1 = i

# Chercher ecart de 1% entre T_Borda et T_Exacte
    if np.abs(((T_exact[i] - T_Borda[i]) / T_exact[i]) - 0.01) <= 0.0005 :
        ilim2 = i
#ilim1 = 23
#ilim2 = 74


fig, ax = plt.subplots(1, 2, num=1, figsize=(8,5), clear=True)
ax = ax.flatten()

xx = np.copy(theta_0_deg)
y0 = np.ones(len(theta_0))
yB = np.copy(T_Borda / T_0)
yE = np.copy(T_exact / T_0)

ax[0].plot(xx,y0,'-',color='k',label='$T_0$')
ax[0].plot(xx,yB,'-',color='r',label='T Borda')
ax[0].plot(xx,yE,'-',color='g',label='T Exacte')

ax[1].plot(xx[0:91],y0[0:91],'-',color='k',label='$T_0$')
ax[1].plot(xx[0:91],yB[0:91],'-',color='r',label='T Borda')
ax[1].plot(xx[0:91],yE[0:91],'-',color='g',label='T Exacte')
ax[1].plot([xx[ilim1],xx[ilim1]],[1.,yE[ilim1]],':m')
ax[1].text(18.4,1.019,str(ilim1)+'°',color='m')
ax[1].plot([xx[ilim2],xx[ilim2]],[yB[ilim2],yE[ilim2]],':b')
ax[1].text(71,1.085,str(ilim2)+'°',color='b')
ax[1].yaxis.tick_right()
ax[1].yaxis.set_label_position("right")

for i in range(2) :
    ax[i].plot(xx[ilim1],1.,'sm')
    ax[i].plot(xx[ilim2],yB[ilim2],'sb')

    ax[i].set_xlabel(r'$\theta_0$ [°]')
    ax[i].set_ylabel(r'T / T$_0$')
    ax[i].legend()


#########################################################################################################################
#%% #########################        Experience Pendule        ##########################################################
#########################################################################################################################


Location = '/Users/kamalyoussef/DATA/Agrégation/Lecon_Montage/Lecon_Physique/MesLecons/P4/Manip_parAdrien/'
name = ["26","56","82"]


def moyenne_glissante(tab,fenetre):
    new_tab = []
    for i in range(len(tab)):
        a = max(0,i-fenetre)
        b = min(i+fenetre,len(tab)-1)
        new_tab.append(np.mean(tab[a:b]))
    return np.array(new_tab)

def portrait_phase(name):
    
    # Lecture des fichiers
    data = []
    with open(Location + name) as csvfile:
        data_line = csv.reader(csvfile, delimiter=';')
        for row in data_line:
            data.append(row)
    
    # creation tableau de valeurs
    theta = []
    time = []
    for i in range(1,len(data)):
        time.append(float(data[i][0].replace(',','.')))
        theta.append(float(data[i][1].replace(',','.')))
    
    # conversion en radians
    theta = np.array(theta)*np.pi/180
    
    # Calculer la dérivée dtheta/dt
    theta_point = []
    for i in range(len(theta)-1):
        theta_point.append((theta[i+1]-theta[i])/(time[i+1]-time[i]))
    
    # Lisser la courbe par une moyenne glissante
    theta_point_avg = moyenne_glissante(theta_point,5)
    
    return theta[:-1],np.array(theta_point_avg)



fig, ax = plt.subplots(1, 1, num=2, clear=True)

for i in name :
    a,b = portrait_phase("theta"+i+".csv")

    #label_plot = r'$\theta_0=$'+i+'°'
    ax.plot(a,b,label=r'$\theta_0=$'+i+'°')
    
    # Copier la courbe à 2pi et -2pi
    ax.plot(a+(2*np.pi),b,'k')
    ax.plot(a-(2*np.pi),b,'k')
    

ax.set_xlabel(r'$\theta$',fontsize=20)   
ax.set_ylabel(r'$\frac{d\theta}{dt}$',fontsize=24)  
ax.set_xticks([-2*np.pi,0,2*np.pi],labels=[r'$-2\pi$','0',r'$2\pi$'])
ax.legend(fontsize=18)
    


#########################################################################################################################
#%% #########################         Portrait de Phase        ##########################################################
#########################################################################################################################

# Pulsation propre en U.A.
omega0 = 4 
# le temps en U.A.
N = 100 
t = np.linspace(0, 5, N) 

# Nb de conditions initiales
Ninit = 12 
# Etats initiaux
dtheta_init_list = np.linspace(-50, 50, Ninit)

# Fonction de l'équation différentielle du mouvement
def eq_diff(etat_courant, t, omega0): 
    return np.array([etat_courant[1], -omega0**2*np.sin(etat_courant[0])])

# Résolution de l'equation differentielle pour chaque condition intiale"
def plot_static_data(ax, omega0):
    for dtheta_init in dtheta_init_list:
        etat_init = np.array([0, dtheta_init/omega0])
        solution = odeint(eq_diff, etat_init, t, args=(omega0,))

        ax.plot(solution[:,0], solution[:,1], color='red', linewidth=1)
        ax.plot(-solution[:,0], solution[:,1], color='red', linewidth=1) # la fonction dtheta(theta) etant paire
        
fig, ax = plt.subplots(1, 2, num=3, sharex=True, sharey=True, clear=True)
ax = ax.flatten()
plot_static_data(ax[0], omega0=5)
plot_static_data(ax[1], omega0=4)

for i in range(2) :
    ax[i].set_ylim([-15.,15.])
    ax[i].set_xlim([-3.2,3.2])
    
    ax[i].set_ylabel(r'$\dot \theta$')
    ax[i].set_xlabel(r'$\theta$')

ax[0].text(-0.4,-1.6,'C=-1.8')
ax[0].text(1.8,-7.3,'C=2')

ax[1].text(2.3,-4.,'C=1')
ax[1].text(1.7,11.7,'C=4')


#########################################################################################################################
#%% #########################           Lien Ep et C          ###########################################################
#########################################################################################################################

# Choisir les theta et les transformer en radian
theta_0_deg = np.arange(-270.,270.+1.,1.)
theta_0 = theta_0_deg * np.pi / 180.

# Energie potentielle
Ep = m * g * L * (1. - np.cos(theta_0))
Ep_90deg = m * g * L
  

# Choisir les Em constantes
C = np.array([-1.8,1.,2.,4.])
Cst_lim = (C/2.) + 1. 

fig, ax = plt.subplots(2, 2, num=4, sharex=True, sharey=True, clear=True)
ax = ax.flatten()
xx = theta_0_deg
yEp = np.copy(Ep / Ep_90deg)

for i in range(4) :
    ylim = np.ones(len(xx)) * Cst_lim[i]
    ax[i].plot(xx,yEp,'-',color='r')
    ax[i].plot(xx,ylim)
    ax[i].set_ylim([-1.,4.])
    ax[i].set_title('C = '+str(C[i]))
    
    ax[i].set_ylabel(r'Ep / mgL')
    ax[i].set_xticks([-270.,-180.,-90.,0.,90.,180.,270.])
    if i==1 or i==3 :
        ax[i].yaxis.tick_right()
        ax[i].yaxis.set_label_position("right")
    if i > 1 : 
        ax[i].set_xlabel(r'$\theta_0$ [°]')



