
# Mission ISS2 – Vérification des résultats des groupes

# =============================================================================
#%% Groupe 1 : Mise en orbite (Thème 2)
# =============================================================================


# Saisir la vitesse orbitale (en km/s) et la période (en minutes)
v_orbitale_kms = 7.8
periode_minutes = 90 

if 7.5 <= v_orbitale_kms <= 8.0 and 88 <= periode_minutes <= 95:
    print("Groupe 1 : Paramètres orbitaux corrects.")
    mission_g1 = True
else:
    print("Groupe 1 : Vérifiez vos calculs de vitesse ou de période.")
    mission_g1 = False

# =============================================================================
#%% Groupe 2 : Panneaux solaires (Thème 3)
# =============================================================================


# Saisir la puissance fournie estimée par les panneaux (en W)
puissance_W = 2200  # Par exemple : 2200 W

if 1800 <= puissance_W <= 2400:
    print("Groupe 2 : L’énergie fournie est suffisante.")
    mission_g2 = True
else:
    print("Groupe 2 : L’énergie n’est pas suffisante ou surdimensionnée.")
    mission_g2 = False

# =============================================================================
#%% Groupe 3 : Communication (Thème 4)
# =============================================================================


# Saisir la fréquence d’émission choisie (en MHz)
frequence_MHz = 1450  # Par exemple : 1450 MHz

if 800 <= frequence_MHz <= 3000:
    print("Groupe 3 : Fréquence compatible avec les communications spatiales.")
    mission_g3 = True
else:
    print("Groupe 3 : Fréquence non compatible. Recalculez.")
    mission_g3 = False

# =============================================================================
#%% Groupe 4 : Moteur et Spectroscopie (Thème 1)
# =============================================================================


# Saisir l’énergie chimique libérée (en kJ) et la raie détectée
energie_kJ = 1200           # Par exemple : 1200 kJ
raie_detectee = 'H2O'       # Par exemple : 'H2O'

if energie_kJ >= 1000 and raie_detectee in ['H2O', 'H2', 'O2']:
    print("Groupe 4 : Propulsion opérationnelle et gaz détecté correct.")
    mission_g4 = True
else:
    print("Groupe 4 : Énergie insuffisante ou gaz inattendu.")
    mission_g4 = False

# =============================================================================
#%% Bilan final de la mission
# =============================================================================

if mission_g1 and mission_g2 and mission_g3 and mission_g4:
    print("\nMission réussie ! Félicitations, vous êtes embauchés à l’ESA ")
else:
    print("\nMission partiellement réussie. Reprenez les calculs et retentez votre chance !")
    


