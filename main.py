import numpy as np
import math
import matplotlib.pyplot as plt

numero_symetrique = int(input("Entrez votre numéro du profil NACA 4 chiffres symétrique NACA00XX. Entrez uniquement les deux derniers chiffres : "))
corde = float(input("Entrez la corde de votre profil (en mètres) : "))
nombre_points = int(input("Entrez le nombre de points que vous souhaitez afficher : "))
distribution = input("Souhaitez-vous une distribution linéaire ou non linéaire ? 'o' pour oui 'n' pour non : ")

# Construction du tableau NumPy en fonction du nombre de points
if distribution == 'o':  # Distribution non linéaire (par exemple, cosinus)
    theta = np.linspace(0, math.pi, nombre_points)
    x_coordinates = 0.5 * (1 - np.cos(theta))

else:  # Distribution linéaire
    x_coordinates = np.linspace(0, 1, nombre_points)

# Calcul des coordonnées y en fonction de la distribution choisie
x_up = x_coordinates*corde
x_down = x_coordinates*corde
y_coordinates = 5 * corde * (0.2969 * np.sqrt(x_coordinates) - 0.126 * x_coordinates - 0.3516 * x_coordinates**2 + 0.2843 * x_coordinates**3 - 0.1036 * x_coordinates**4)
y_up = y_coordinates*corde
y_down = (-1)*y_coordinates*corde
# Affichage des coordonnées

epaisseur_maximale = np.max(y_coordinates)
position_epaisseur_maximale = x_coordinates[np.argmax(y_coordinates)]

print("Épaisseur maximale :", epaisseur_maximale)
print("Position de l'épaisseur maximale le long de la corde :", position_epaisseur_maximale)

print("Coordonnées x:", x_coordinates)
print("Coordonnées y:", y_coordinates)

plt.plot(x_up, y_up, label='extrados',color ='r')
plt.plot(x_down, y_down, label='intrados',color='b')
plt.axhline(0, color='black', linewidth=0.8)  # Ligne horizontale pour l'axe x
plt.grid(True, linestyle='--', alpha=0.6)
plt.title(f"Profil NACA00{numero_symetrique}")
plt.xlabel('Position le long de la corde')
plt.ylabel('Épaisseur')
plt.legend()
plt.show()