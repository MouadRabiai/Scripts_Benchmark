import matplotlib.pyplot as plt
import numpy as np

# Configurations et leurs fréquences maximales
configurations = [
    "WAESP32AU1V010", "WAESP32AU1V010M", "WAESP32AU1V010IF1", "WAESP32AU1V010JAlBr",
    "WAESP32AU1V010F", "WAESP32AU1V010IF1", "WAESP32AU1V010FIF", "WAESP32AU1V010FIFJalBr",
    "WAESP32AU1V010JalBr2", "WAESP32AU1V010NoNlp", "WAESP32AU1V010FIFNoNlp",
    "WAESP32AU1V010FIFNoNlpNoMul", "WAESP32AU1V010FIFNoNlpNoHpm",
    "WAESP32AU1V010FIFNoNlpNoMulNoHpm", "WAESP32AU1V010FIFNoNlpNoHpmMulReg",
    "WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2",
    "WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2DmemWReg",
    "WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2DmemReg", "WAESP32AU1V011", "WAESP32AU1V030"
]

frequencies = [
    58, 77, 82, 61, 78, 82, 72, 61, 61, 75, 76, 83, 70, 99, 84, 90, 88, 103, 56, 59
]

# Créer les données pour le graphique
index = np.arange(len(configurations))
bar_width = 0.5  # Largeur des barres

fig, ax = plt.subplots(figsize=(14, 8))  # Ajuster la taille du graphique

# Créer un graphique à barres
ax.barh(index, frequencies, bar_width, color='skyblue', label='Fréquence (MHz)')

ax.set_xlabel('Fréquence maximale (MHz)')
ax.set_title('Fréquence maximale par configuration')
ax.set_yticks(index)
ax.set_yticklabels(configurations)
ax.invert_yaxis()  # Inverser l'axe y pour que les barres commencent en haut
ax.legend()

plt.tight_layout()
plt.show()
