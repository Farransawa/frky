

import numpy as np


R = 8.314      # Constante des gaz parfaits [J/mol/K]
P = 1.013e5    # Pression air [Pa]
M = 29.        # Masse molaire air [g/mol]
M *= 1e-3      # [kg/mol]
CtoK = 273.15  # Aller de °C à K

T_C = 25       # [°C]
T_K = T_C + CtoK
 
# Calcul de la masse volumique de l'air
rho_theo = (M * P) / (R * T_K)   # kg/m3

# Calcul de zscore
rho_exp =  1.394    # kg/m3
urho_exp =  1.5e-2   # kg/m3
zscore = np.abs(rho_theo-rho_exp) / urho_exp

print("A {}°C la valeur de rho est : {} kg/m3".format(T_C,round(rho_theo,3)))
print("La valeur expérimentale est : {} kg/m3".format(round(rho_exp,3)))
print("Le zscore est : {} sigma".format(round(zscore,2)))
