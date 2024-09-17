import matplotlib.pyplot as plt
import numpy as np

# Données des hits et des misses pour chaque programme et chaque configuration
programmes = [
    "aha-mont64", "crc32", "cubic", "edn", "huffbench", "matmult-int", 
    "md5sum", "minver", "nbody", "nettle-aes", "nettle-sha256", 
    "nsichneu", "picojpeg", "primecount", "qrduino", "sglib-combined", 
    "slre", "st", "statemate", "tarfind", "ud", "wikisort"
]

hits_WAESP32AU1V210 = [
    5083921, 4590638, 13221435, 4787584, 4101340, 5345333, 
    2576925, 8765202, 11056587, 7088982, 5727252, 5384637, 
    6863441, 6395150, 4630404, 4537400, 4502682, 7344268, 
    3184468, 1658235, 5310215, 4417032
]

misses_WAESP32AU1V210 = [
    26503, 5604, 1655271, 25271, 10896, 91255, 
    19500, 771866, 1371520, 925961, 902045, 985720, 
    205442, 81, 8196, 35559, 190870, 948738, 
    210102, 15905, 183144, 494394
]

hits_WAESP32AU1V210Set4Data4 = [
    5078821, 5125621, 13591887, 4849483, 4116925, 6465002, 
    2617355, 9724471, 11519622, 7389418, 5763008, 5384649, 
    7402652, 6395182, 4634533, 4800982, 5026383, 7427956, 
    3236597, 1681626, 6017540, 4416772
]

misses_WAESP32AU1V210Set4Data4 = [
    52282, 101816, 2122941, 52694, 14532, 441074, 
    31262, 1608763, 1873981, 1244815, 975528, 985723, 
    479462, 107, 11727, 149553, 499448, 1463280, 
    367074, 18354, 630695, 569170
]

# Indices pour les programmes
index = np.arange(len(programmes))

# Largeur des barres dans le graphique
bar_width = 0.35

# Création de la première figure comparant les hits
fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.bar(index, hits_WAESP32AU1V210, bar_width, label='WAESP32AU1V210 Hits')
ax1.bar(index + bar_width, hits_WAESP32AU1V210Set4Data4, bar_width, label='WAESP32AU1V210Set4Data4 Hits')

ax1.set_xlabel('Programme')
ax1.set_ylabel('Hits')
ax1.set_title('Comparaison des Hits pour chaque configuration et chaque programme')
ax1.set_xticks(index + bar_width / 2)
ax1.set_xticklabels(programmes, rotation=90)
ax1.legend()

# Ajustement de la mise en page pour éviter les chevauchements de texte
plt.tight_layout()

# Création de la deuxième figure comparant les misses
fig, ax2 = plt.subplots(figsize=(14, 8))

ax2.bar(index, misses_WAESP32AU1V210, bar_width, label='WAESP32AU1V210 Misses')
ax2.bar(index + bar_width, misses_WAESP32AU1V210Set4Data4, bar_width, label='WAESP32AU1V210Set4Data4 Misses')

ax2.set_xlabel('Programme')
ax2.set_ylabel('Misses')
ax2.set_title('Comparaison des Misses pour chaque configuration et chaque programme')
ax2.set_xticks(index + bar_width / 2)
ax2.set_xticklabels(programmes, rotation=90)
ax2.legend()

# Ajustement de la mise en page pour éviter les chevauchements de texte
plt.tight_layout()

# Afficher les deux graphiques
plt.show()
