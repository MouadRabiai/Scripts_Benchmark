import matplotlib.pyplot as plt
import numpy as np

# Liste des benchmarks
benchmarks = [
    "aha-mont64", "crc32", "cubic", "edn", "huffbench", 
    "matmult-int", "md5sum", "minver", "nbody", "nettle-aes",
    "nettle-sha256", "nsichneu", "picojpeg", "primecount", 
    "qrduino", "sglib-combined", "slre", "st", "statemate", 
    "tarfind", "ud", "wikisort"
]

# CPI pour les deux configurations
cpi_WAESP32AU1V210 = [1.186, 1.154, 3.136, 1.211, 1.439, 1.514, 1.189, 2.794, 2.898, 2.632, 
                      2.791, 5.473, 1.540, 1.899, 1.289, 1.696, 2.073, 3.221, 3.142, 2.103, 
                      1.814, 3.076]

cpi_WAESP32AU1V210Set4Data4 = [1.235, 1.673, 3.621, 1.638, 1.763, 2.827, 1.292, 4.142, 3.489, 3.159, 
                               2.962, 5.923, 2.103, 2.294, 1.537, 2.337, 3.222, 4.181, 4.434, 2.221, 
                               3.216, 3.354]

# Nombre total de configurations
num_configs = 2

# Paramètres de l'affichage
index = np.arange(len(benchmarks))
bar_width = 0.35  

# Création de la figure
fig, ax = plt.subplots(figsize=(15, 8))

# Plot des barres pour chaque configuration
ax.bar(index, cpi_WAESP32AU1V210, bar_width, label='WAESP32AU1V210')
ax.bar(index + bar_width, cpi_WAESP32AU1V210Set4Data4, bar_width, label='WAESP32AU1V210Set4Data4')

# Paramètres du graphique
ax.set_xlabel('EXEC NAME')
ax.set_ylabel('CPI')
ax.set_title('CPI par programme pour WAESP32AU1V210 et WAESP32AU1V210Set4Data4')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(benchmarks, rotation=90)
ax.legend()

# Affichage du graphique
plt.tight_layout()
plt.show()
