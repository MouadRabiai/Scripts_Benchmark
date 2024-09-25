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
    5060703, 4588237, 12995199, 4783734, 4100540, 5302252,
    2574867, 8503385, 10861420, 7008968, 5702278, 5384635, 
    6837935, 6395148, 4628682, 4525032, 4423600, 6996087,
    3068499, 1658232, 5174242, 4371138
]

misses_WAESP32AU1V210 = [
    49298, 8005, 1855689, 28991, 11594, 134336,
    20762, 1017927, 1550316, 1013581, 924001,
    985722, 226622, 83, 9691, 47872, 263157, 1265370,
    275881, 15908, 300640, 533495

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
