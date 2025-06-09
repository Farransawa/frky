

import numpy as np


# Puissance 1
U1 = 55       # V 
U1_incert = ( (0.006 * U1) + (10. * 0.01) ) #/ np.sqrt(3)
i1 = 75  *1.0e-3  # A
i1_incert = ( (0.01 * i1) +  (10. * 0.0001) ) #/ np.sqrt(3)
P1 = U1 * i1
# Propagation d'incertitude
P1_incert = P1 * np.sqrt((U1_incert/U1)**2 + (i1_incert/i1)**2)


# Puissance 2
U2 = 35       # V 
U2_incert = ( (0.006 * U2) + (10. * 0.01) ) #/ np.sqrt(3)
i2 = 650  *1.0e-3  # A
i2_incert = ( (0.01 * i2) +  (10. * 0.0001) ) #/ np.sqrt(3)
P2 = U2 * i2
# Propagation d'incertitude
P2_incert = P2 * np.sqrt((U2_incert/U2)**2 + (i2_incert/i2)**2)


print("Puissance 1 : {} ± {} W".format(np.round(P1,3),np.round(P1_incert,3)))
print("Puissance 2 : {} ± {} W".format(np.round(P2,3),np.round(P2_incert,3)))


#%%


# Ajustement fct Affine 1
A1 = -2.8e-1           # g/s
A1_incert = 3.5e-4     # g/s

# Ajustement fct Affine 2
A2 = -9.1e-2           # g/s
A2_incert = 2.6e-4     # g/s


# Conversion d'unité
A1 = A1 * 1.0e-3     # kg/s
A2 = A2 * 1.0e-3     # kg/s
A1_incert *= 1.0e-3     # kg/s
A2_incert *= 1.0e-3     # kg/s


# Chaleur latente de vaporisation
Lv_tab = 199.2  # kJ/kg
Lv_exp = (P1 - P2) * 1.0e-3 / (A2 - A1)   # kJ/kg


# Incertitude-type
Lv_incert = Lv_exp * np.sqrt((P2_incert/P2)**2 + (P1_incert/P1)**2 + (A1_incert/A1)**2 + (A2_incert/A2)**2)
zscore = np.abs(Lv_tab - Lv_exp) / Lv_incert


print("Chaleur Latente : {} ± {} kJ/kg".format(np.round(Lv_exp,1),np.round(Lv_incert,1)))
print("Zscore = {}".format(zscore))


