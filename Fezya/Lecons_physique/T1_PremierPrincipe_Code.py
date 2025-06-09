

import numpy as np

#########################################################################
###############   Simulation Monte Carlo Sans Plomb    ##################
#########################################################################

# Les mesures de masses
MCalo = 474.90                 # g
MCalo_MeauF = 565.78           # g
MCalo_MeauF_MeauC = 643.41     # g
MeauF = (MCalo_MeauF - MCalo)*1.0e-3                 # kg
MeauC = (MCalo_MeauF_MeauC - MCalo_MeauF)*1.0e-3     # kg

# Les mesures de températures
TeauC = 97.2     # °C
TeauF = 22.4     # °C
TeauEq = 53.4    # °C

# La capacité thermique massique de l'eau
C_eau = 4180   # J/kg/K

# Nb points 
N = 100000   

# Listes des masses aléatoires selon une loi normale
mf = np.random.normal(MeauF, 0.0002, N)
mc = np.random.normal(MeauC, 0.0002, N)

# Listes des Températures aléatoires selon une loi normale
Tf = np.random.normal(TeauF, 0.1, N)
Tc = np.random.normal(TeauC, 0.5, N)
Teq = np.random.normal(TeauEq, 0.5, N)

# Calculer la capacité thermique du calorimètre
C_calo = C_eau * ((mc*(Tc - Teq)) + (mf*(Tf - Teq))) / (Teq - Tf)
C_calo_moy = np.mean(C_calo) 
C_calo_sig = np.std(C_calo)

print("La capacité thermique du calorimètre est ({:.2f} ± {:.2f}) J/K".format(C_calo_moy,C_calo_sig))
print("En masse d'eau équivalente = {:.1f} g".format(C_calo_moy*1000/C_eau))

C_calo_Const = 100.     # J/K
zscore = np.abs(C_calo_Const - C_calo_moy)/C_calo_sig

print("\nLa valeur du constructeur = {} J/K ce qui équivaut à {} g d'eau".format(C_calo_Const,round(C_calo_Const*1000/C_eau)))
print("Le Zscore = {:.2f} sigma".format(zscore))

#########################################################################
#%%############   Simulation Monte Carlo Avec Plomb    ##################
#########################################################################


# Les mesures de masses
MCalo = 474.9                      # g
MCalo_MeauF = 552.37               # g
MCalo_MeauF_MPb = 621.17           # g
MCalo_MeauF_MPb_MeauC = 727.56     # g
MeauF = (MCalo_MeauF - MCalo)*1.0e-3                        # kg
MPb = (MCalo_MeauF_MPb - MCalo_MeauF)*1.0e-3                # kg
MeauC = (MCalo_MeauF_MPb_MeauC - MCalo_MeauF_MPb)*1.0e-3    # kg

# Les mesures de températures
TeauC = 95.2     # °C
TeauF = 22.6     # °C
TeauEq = 59.1    # °C


# Nb points 
N = 100000   


# Listes des masses aléatoires selon une loi normale
mf = np.random.normal(MeauF, 0.0002, N)
mc = np.random.normal(MeauC, 0.0002, N)
mp = np.random.normal(MPb, 0.0002, N)

# Listes des Températures aléatoires selon une loi normale
Tf = np.random.normal(TeauF, 0.1, N)
Tc = np.random.normal(TeauC, 0.5, N)
Teq = np.random.normal(TeauEq, 0.5, N)

# Calculer la capacité thermique du calorimètre
C_Pb = ((C_eau*((mc*(Teq - Tc)) + (mf*(Teq - Tf)))) + C_calo_moy*(Teq - Tf)) / (mp*(Tf - Teq))
C_Pb_moy = np.mean(C_Pb)
C_Pb_sig = np.std(C_Pb)

print("La capacité thermique massique du plomb est ({:.2f} ± {:.2f}) J/kg/K".format(C_Pb_moy,C_Pb_sig))

C_Pb_Tab = 130     # J/kg/K
zscore = np.abs(C_Pb_Tab - C_calo_moy)/C_calo_sig

print("\nLa valeur tabulee est = {} J/kg/K".format(C_Pb_Tab))
print("Le Zscore = {:.2f} sigma".format(zscore))


