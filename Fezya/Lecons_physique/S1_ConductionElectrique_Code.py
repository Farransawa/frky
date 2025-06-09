

import numpy as np
import math



# La résistivité expérimentale
rho_exp =  1.394e-8     # [Ohm.m]
urho_exp =  1.5e-10     # [Ohm.m]

# La résistivité tabulée
rho_tab = 1.678e-8      # [Ohm.m]


# La conductivité

sig_exp = 1. / rho_exp  # [S.m-1]
sig_tab = 1. / rho_tab  # [S.m-1]

# Propagation d'erreur
usig_exp = (sig_exp * urho_exp) / rho_exp

# Trouver l'exposant commun pour l'affichage
expo = int(math.floor(math.log10(abs(sig_exp))))
# Normaliser les valeurs pour l'affichage
sig_exp_noExpo = sig_exp / (10 ** expo)
usig_exp_noExpo = usig_exp / (10 ** expo)


print("La conductivité tabulée est : {:.2e} S·m⁻¹".format(sig_tab))
print("La conductivité trouvée est : ({:.2f} ± {:.2f})e+{:02d} S·m⁻¹".format(sig_exp_noExpo, usig_exp_noExpo,expo))


# Calcul de zscore
zscore = np.abs(sig_exp-sig_tab) / usig_exp
print("Le zscore est : {} sigma".format(round(zscore,2)))
