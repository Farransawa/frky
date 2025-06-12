
# Mission ISS2 – Vérification des résultats des groupes

# =============================================================================
#%% Groupe 1 : Mise en orbite (Thème 2)
# =============================================================================


# Saisir la vitesse orbitale (en km/s) et la période (en minutes)
v_orbitale = 7.7
periode = 90 

if 7.5 <= v_orbitale <= 7.8 and 88 <= periode <= 92:
    print("Groupe 1 : Paramètres orbitaux corrects.")
    mission_g1 = True
else:
    print("Groupe 1 : Vérifiez vos calculs de vitesse ou de période.")
    mission_g1 = False

# =============================================================================
#%% Groupe 2 : Panneaux solaires (Thème 3)
# =============================================================================


# Saisir le flux reçu par le satellite (en W m-2)
flux = 1368  
# Saisir la surface de panneaux nécessaire (en m2)
S_panneaux = 735


if 1300 <= flux <= 1400 and 700 <= S_panneaux <= 800 :
    print("Groupe 2 : Paramètres énergétiques corrects.")
    mission_g2 = True
else:
    print("Groupe 2 : Vérifiez vos calculs de flux ou de surface de panneaux.")
    mission_g2 = False

# =============================================================================
#%% Groupe 3 : Communication (Thème 4)
# =============================================================================


# Saisir la longueur d'onde d’émission (en m)
LongueurOnde = 0.125  
# Saisir le diamètre d’antenne (en m)
diametre_antenne = 61

if 0.12 <= LongueurOnde <= 0.13 and 55 <= diametre_antenne <= 70 :
    print("Groupe 3 : Paramètres de communication corrects.")
    mission_g3 = True
else:
    print("Groupe 3 : Vérifiez vos calculs de longueur d'onde ou de diamètre d'antenne.")
    mission_g3 = False

# =============================================================================
#%% Groupe 4 : Moteur et Spectroscopie (Thème 1)
# =============================================================================


# Saisir le nombre de moles nécessaires et la raie détectée dans le moteur défectueux
moles = 1748          
raie_detectee = 'Na'       

if 1700 <= moles <= 1800 and raie_detectee in ['Na', 'CO', 'NO']:
    print("Groupe 4 : Paramètres du moteur corrects.")
    mission_g4 = True
else:
    print("Groupe 4 : Vérifiez vos calculs.")
    mission_g4 = False

# =============================================================================
#%% Bilan final de la mission
# =============================================================================

if mission_g1 and mission_g2 and mission_g3 and mission_g4:
    print("\nMission réussie ! Félicitations, vous êtes embauchés à l’ESA ")
else:
    print("\nMission partiellement réussie. Reprenez les calculs et retentez votre chance !")
    


