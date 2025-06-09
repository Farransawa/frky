import numpy as np
import matplotlib.pyplot as plt

# Constantes physiques
h = 6.626e-34       # constante de Planck (J.s)
c = 3.00e8           # vitesse de la lumière (m/s)
kB = 1.381e-23       # constante de Boltzmann (J/K)

# Loi de Planck (u_nu)
def planck_nu(nu, T):
    return (8 * np.pi * h * nu**3) / (c**3 * (np.exp(h * nu / (kB * T)) - 1))

# Loi de Rayleigh-Jeans (approximation pour basses fréquences)
def rayleigh_jeans(nu, T):
    return (8 * np.pi * nu**2 * kB * T) / c**3

# Loi de Wien (approximation pour hautes fréquences)
def wien(nu, T):
    return (8 * np.pi * h * nu**3) / (c**3) * np.exp(-h * nu / (kB * T))

# Plage de fréquences (Hz)
nu = np.linspace(1e11, 3e15, 1000)  # de l'infrarouge à l'ultraviolet
T = 5800  # température du Soleil, en K

# Calcul des spectres
nu_planck = planck_nu(nu, T)
nu_rj = rayleigh_jeans(nu, T)
nu_wien = wien(nu, T)

# Tracé
plt.figure(figsize=(10, 6))
plt.plot(nu, nu_planck, label="Planck", color='black')
plt.plot(nu, nu_rj, label="Rayleigh-Jeans", linestyle='--', color='blue')
plt.plot(nu, nu_wien, label="Wien", linestyle='--', color='red')

plt.xlabel("Fréquence ν (Hz)")
plt.ylabel(r"$u_ν$ (J/m³/Hz)")
plt.title("Spectre d'un corps noir à T = {} K".format(T))
plt.legend()
plt.grid(True)
plt.yscale('log')
plt.xscale('log')
plt.tight_layout()
plt.show()


