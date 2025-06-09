import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Système du 2nd ordre (type filtre passe-bas ou oscillateur amorti)
def second_order_response(zeta, omega_n, precision, t):
    # Calcul de la fréquence propre amortie si le système est sous-amorti
    omega_d = omega_n * np.sqrt(1 - zeta**2) if zeta < 1 else 0
    if zeta < 1:
        # Réponse sous-amortie
        y = 1 - (1 / np.sqrt(1 - zeta**2)) * np.exp(-zeta * omega_n * t) * \
               np.sin(omega_d * t + np.arccos(zeta))
    elif zeta == 1:
        # Réponse critique
        y = 1 - np.exp(-omega_n * t) * (1 + omega_n * t)
    else:
        # Réponse sur-amortie
        s1 = -omega_n * (zeta - np.sqrt(zeta**2 - 1))
        s2 = -omega_n * (zeta + np.sqrt(zeta**2 - 1))
        A = (s2 / (s2 - s1))
        B = 1 - A
        y = 1 - A * np.exp(s1 * t) - B * np.exp(s2 * t)
    return y * precision  # Application du facteur de précision

# Génère un vecteur temps de 0 à 10 s avec 1000 points
t = np.linspace(0, 10, 1000)

# Valeurs initiales des paramètres
zeta0 = 0.7            # Amortissement initial
omega_n0 = 2.0         # Pulsation propre initiale
precision0 = 1.0       # Précision cible initiale
response = second_order_response(zeta0, omega_n0, precision0, t)  # Calcul initial

# Initialisation de la figure et des axes matplotlib
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.45)  # Réserve de la place pour les curseurs et boutons

# Tracé de la réponse initiale
l, = plt.plot(t, response, lw=2)

# Ligne horizontale représentant la valeur finale cible (fixée à 1.0)
final_line = ax.axhline(y=1.0, color='gray', linestyle='--', label="Valeur cible (1.0)")

# Zone grisée représentant une tolérance de ±5% autour de la cible
confidence_band = ax.fill_between(t, 0.95, 1.05, color='gray', alpha=0.2, label="Zone à 95%")

# Réglages du graphique
ax.set_ylim(-0.5, 2)
ax.set_title("Réponse d'un système bouclé du 2e ordre",fontsize=16)
ax.set_xlabel("Temps")
ax.set_ylabel("Réponse")
ax.legend()

# Création des curseurs pour modifier ζ, ωₙ et précision
ax_zeta = plt.axes([0.25, 0.1, 0.65, 0.03])
ax_omega = plt.axes([0.25, 0.15, 0.65, 0.03])
ax_precision = plt.axes([0.25, 0.2, 0.65, 0.03])

s_zeta = Slider(ax_zeta, 'Stabilité (ζ)', 0.0, 2.0, valinit=zeta0)  # Curseur pour ζ
s_omega = Slider(ax_omega, 'Rapidité (ωₙ)', 0.1, 10.0, valinit=omega_n0)  # Curseur pour ωₙ
s_precision = Slider(ax_precision, 'Précision', 0.1, 2.0, valinit=precision0)  # Curseur précision

# Bouton de reset des curseurs
reset_ax = plt.axes([0.8, 0.025, 0.1, 0.04])
reset_button = Button(reset_ax, 'Reset', hovercolor='0.975')

# Fonction de mise à jour du graphique selon les valeurs des curseurs
def update(val):
    zeta = s_zeta.val
    omega_n = s_omega.val
    precision = s_precision.val
    l.set_ydata(second_order_response(zeta, omega_n, precision, t))  # Met à jour la courbe
    fig.canvas.draw_idle()

# Connexion des curseurs à la fonction update
s_zeta.on_changed(update)
s_omega.on_changed(update)
s_precision.on_changed(update)

# Fonction pour remettre tous les curseurs à leurs valeurs initiales
def reset(event):
    s_zeta.reset()
    s_omega.reset()
    s_precision.reset()

# Connexion du bouton reset à la fonction reset
reset_button.on_clicked(reset)
