import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# Données des benchmarks
benchmarks = [
    "aha-mont64", "crc32", "cubic", "edn", "huffbench",
    "matmult-int", "md5sum", "minver", "nbody", "nettle-aes",
    "nettle-sha256", "nsichneu", "picojpeg", "primecount",
    "qrduino", "sglib-combined", "slre", "st", "statemate",
    "tarfind", "ud", "wikisort"
]

# CPI data for each configuration
configs = {
    "WAESP32AU1V010FIFNoNlpNoHpmMulReg": [1.979, 2.273, 2.110, 1.997, 2.360, 2.324, 2.049, 2.438, 2.264, 1.552,
                                          1.551, 3.164, 1.872, 2.896, 1.919, 2.430, 2.350, 2.257, 1.864, 2.918,
                                          2.445, 2.437],
    "WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2": [1.979, 2.273, 2.110, 1.997, 2.360, 2.324, 2.049, 2.438, 2.264, 1.552,
                                            1.551, 3.164, 1.872, 2.896, 1.919, 2.430, 2.350, 2.257, 1.864, 2.918,
                                              2.445, 2.437],
    "WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2DmemWreg": [1.979, 2.273, 2.111, 1.997, 2.360, 2.324, 2.049, 2.438, 2.264, 1.552,
                                                     1.551, 3.164, 1.872, 2.896, 1.919, 2.430, 2.350, 2.257, 1.864, 2.918,
                                                     2.445, 2.437],
    "WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2DmemReg": [1.980, 2.318, 2.133, 2.139, 2.409, 2.439, 2.051, 2.456, 2.271, 1.575,
                                                    1.569, 3.712, 1.922, 3.071, 2.004, 2.575, 2.446, 2.265, 2.110, 2.939,
                                                    2.481, 2.499],
    "WAESP32AU1V010NoNlp": [1.341, 1.773, 1.520, 1.746, 1.667, 1.936, 1.349, 1.654, 1.527, 1.065,
                            1.059, 2.786, 1.430, 2.333, 1.472, 1.859, 1.700, 1.601, 1.447, 2.361,
                            1.790, 1.813],
    "WAESP32AU1V010NoHpm": [1.341, 1.773, 1.520, 1.746, 1.667, 1.936, 1.349, 1.654, 1.527, 1.065,
                            1.059, 2.786, 1.430, 2.333, 1.472, 1.859, 1.700, 1.601, 1.447, 2.361,
                            1.790, 1.813],
    "WAESP32AU1V010NoNlp2": [1.413, 1.955, 1.592, 1.842, 1.952, 2.176, 1.461, 1.756, 1.588, 1.081,
                             1.088, 3.319, 1.546, 2.672, 1.628, 2.159, 1.911, 1.648, 1.699, 2.539,
                             1.956, 1.956],
    "WAESP32AU1V010NoHpm2": [1.184, 1.274, 1.537, 1.433, 1.604, 1.749, 1.126, 1.634, 1.485, 1.048,
                             1.070, 3.319, 1.286, 2.205, 1.467, 1.850, 1.685, 1.579, 1.586, 1.800,
                             1.677, 1.678],
    "WAESP32AU1V010NoHpm2Btb16": [1.186, 1.274, 1.559, 1.434, 1.604, 1.749, 1.126, 1.738, 1.516, 1.048,
                                  1.071, 3.319, 1.310, 2.205, 1.471, 1.871, 1.803, 1.627, 1.679, 1.801,
                                  1.885, 1.697],
    "WAESP32AU1V010NoHpm2Btb8": [1.186, 1.274, 1.559, 1.434, 1.604, 1.749, 1.126, 1.738, 1.516, 1.048,
                                  1.071, 3.319, 1.310, 2.205, 1.471, 1.871, 1.803, 1.627, 1.679, 1.801,
                                  1.885, 1.697],
    "WAESP32AU1V010NoHpm2Btb16IFReg": [1.915, 1.773, 2.161, 1.557, 2.202, 1.816, 1.968, 2.557, 2.311, 1.566,
                                       1.568, 3.697, 1.807, 2.843, 1.867, 2.443, 2.511, 2.311, 2.025, 2.392,
                                       2.564, 2.411],
    "WAESP32AU1V010NoHpm2Btb8IFReg": [1.915, 1.773, 2.161, 1.557, 2.202, 1.816, 1.968, 2.557, 2.311, 1.566,
                                      1.568, 3.697, 1.807, 2.843, 1.867, 2.443, 2.511, 2.311, 2.025, 2.392,
                                      2.564, 2.411]
}

# Regrouper les configurations qui ont exactement le même CPI pour tous les benchmarks
grouped_cpi = defaultdict(list)
for config_name, cpis in configs.items():
    # Utiliser un tuple des CPI pour comparer sur tous les benchmarks
    cpi_tuple = tuple(cpis)
    grouped_cpi[cpi_tuple].append(config_name)

# Couleurs pour les groupes de configurations
colors = plt.get_cmap('tab20').colors
color_mapping = {}  # Associer une couleur à chaque groupe de configurations
color_index = 0

# Création du graphique
fig, ax = plt.subplots(figsize=(25, 15))  # Augmenter la taille de la figure pour accommoder les barres plus larges

# Paramètres de largeur et décalage des barres
bar_width = 0.6  # Augmenter la largeur des barres
spacing_between_programs = 5  # Augmenter l'espacement entre les benchmarks

# Positions des barres avec un espacement ajouté
bar_positions = np.arange(len(benchmarks)) * (1 + spacing_between_programs)

# Déplacement initial pour ajuster les barres côte à côte
bar_offset = 0

# Tracer les barres pour chaque groupe de configurations ayant le même CPI
for cpi_tuple, config_names in grouped_cpi.items():
    # Attribuer une couleur unique pour ce groupe
    bar_color = colors[color_index % len(colors)]
    
    # Tracer les barres pour ce groupe
    bars = ax.bar(bar_positions + bar_offset, cpi_tuple, width=bar_width, color=bar_color, label=', '.join(config_names))

    # Ajouter les pourcentages au-dessus des barres
    for i, bar in enumerate(bars):
        height = bar.get_height()
        mean_cpi = np.mean([configs[config][i] for config in configs])
        percent_diff = ((height - mean_cpi) / mean_cpi) * 100
        ax.annotate(f'{percent_diff:.1f}%',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=7.5, rotation=90)
    
    # Stocker la couleur pour chaque configuration
    for config_name in config_names:
        color_mapping[config_name] = bar_color
    
    # Incrémenter le décalage pour placer la prochaine barre à côté
    bar_offset += bar_width
    color_index += 1

# Personnalisation des axes et du titre
ax.set_xlabel('Nom du benchmark', fontsize=12)
ax.set_ylabel('CPI', fontsize=12)
ax.set_title('Comparaison de CPI par programme avec regroupement des configurations ayant le même CPI', fontsize=14)
ax.set_xticks(bar_positions + bar_offset / 2)
ax.set_xticklabels(benchmarks, rotation=90, fontsize=10)

# Création de la légende
legend_handles = [plt.Rectangle((0, 0), 1, 1, color=color_mapping[config_name]) for config_name in color_mapping]
legend_labels = list(color_mapping.keys())
ax.legend(legend_handles, legend_labels, title="Configurations", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)

# Ajustement de la mise en page
plt.tight_layout()

# Affichage du graphique
plt.show()
