import matplotlib.pyplot as plt
import numpy as np

# Noms des benchmarks
benchmarks = [
    "aha-mont64", "crc32", "cubic", "edn", "huffbench", 
    "matmult-int", "md5sum", "minver", "nbody", "nettle-aes",
    "nettle-sha256", "nsichneu", "picojpeg", "primecount", 
    "qrduino", "sglib-combined", "slre", "st", "statemate", 
    "tarfind", "ud", "wikisort"
]

# Nombre d'instructions pour chaque configuration de processeur
# Les listes doivent être remplies avec les nombres d'instructions appropriés pour chaque benchmark
instr_WAESP32AU1V010 = [
    4531262, 3831161, 7074897, 3499382, 2450506, 3183124, 2046782, 4927371, 3473819,
    4406508, 3992435, 2236759, 3787005, 2148524, 2793650, 2545397, 2468883, 3911670,
    1141116, 1016017, 3349203, 125475
]

instr_WAESP32AU1V010M = [
    10374236, 5746041, 26107387, 74269182, 2598467, 28448532, 2047394, 12995961, 13466277,
    4754544, 4015235, 2236759, 4706577, 5145879, 5258245, 2830554, 2590543, 16327788,
    1278596, 5196219, 6513601, 3087842
]

instr_WAESP32AU1V010IF1 = [
    10374236, 5746041, 26107387, 74492250, 2598466, 28448531, 2047393, 12995961, 13466277,
    4789332, 4030435, 2236759, 4754810, 5145878, 5263484, 2831974, 2590543, 16327788,
    1318858, 5196218, 6513601, 3087842
]

instr_WAESP32AU1V010JalBr = [
    10374236, 5746040, 26107387, 74492250, 2598466, 28448531, 2047393, 12995961, 13466277,
    4789332, 4030435, 2236759, 4754810, 5145878, 5322644, 2826232, 2590543, 16327788,
    1317876, 5196218, 6513601, 3087842
]

instr_WAESP32AU1V010F = [
    4531262, 3831161, 6637287, 3919331, 2598467, 3183124, 2046782, 4964001, 3478653,
    4427412, 4015235, 2236759, 4134861, 2148524, 3168775, 2622218, 2590543, 3936305,
    1278596, 1037258, 3358071, 1266807
]

instr_WAESP32AU1V010FIF = [
    4531262, 3831161, 6033657, 4040522, 2598466, 3183123, 2046781, 4964001, 3478553,
    4462356, 4030435, 2236759, 4214355, 2148523, 3158114, 2623638, 2590543, 3936305,
    1318858, 1037257, 3358071, 1265262
]

instr_WAESP32AU1V010FIFJalBr = [
    4531262, 3831160, 7079337, 3994412, 2598466, 3183123, 2046781, 4929591, 3475620,
    4462356, 4030435, 2236759, 4128297, 2148523, 3194089, 2617896, 2590543, 3921134,
    1317876, 1036978, 3358071, 1256852
]

instr_WAESP32AU1V010FIFNoNlp = [
    4531262, 3831160, 7079337, 3999197, 2598466, 3183123, 2046781, 4929591, 3475620,
    4463292, 4030435, 2236759, 4124679, 2148523, 3158064, 2628017, 2590543, 3921134,
    1317876, 1036978, 3358071, 1256852
]

instr_WAESP32AU1V010FIFNoNlpNoMul = [
    10374236, 5746040, 26107387, 74273706, 2598466, 28448531, 2047393, 12995961, 13466277,
    4790268, 4030435, 2236759, 4740819, 5145878, 5264354, 2836353, 2590543, 16327788,
    1317876, 5196218, 6513601, 3087842
]

instr_WAESP32AU1V010FIFNoNlpNoMulNoHpm = [
    10374236, 5746040, 26107387, 74273706, 2598466, 28448531, 2047393, 12995961, 13466277,
    4790268, 4030435, 2236759, 4740819, 5145878, 5264354, 2836353, 2590543, 16327788,
    1317876, 5196218, 6513601, 3087842
]


# Nombre de configurations
num_configs = 10

# Créer les données pour les graphiques
index = np.arange(len(benchmarks))
bar_width = 0.08  # Ajuster la largeur pour que les barres ne se chevauchent pas

fig, ax = plt.subplots(figsize=(20, 10))  # Ajuster la taille pour une meilleure visibilité

# Définir les barres sur le graphique
configs = [
    instr_WAESP32AU1V010, instr_WAESP32AU1V010M, instr_WAESP32AU1V010IF1, instr_WAESP32AU1V010JalBr,
    instr_WAESP32AU1V010F, instr_WAESP32AU1V010FIF, instr_WAESP32AU1V010FIFJalBr, instr_WAESP32AU1V010FIFNoNlp,
    instr_WAESP32AU1V010FIFNoNlpNoMul, instr_WAESP32AU1V010FIFNoNlpNoMulNoHpm
]
labels = [
    'WAESP32AU1V010', 'WAESP32AU1V010M', 'WAESP32AU1V010IF1', 'WAESP32AU1V010JalBr',
    'WAESP32AU1V010F', 'WAESP32AU1V010FIF', 'WAESP32AU1V010FIFJalBr', 'WAESP32AU1V010FIFNoNlp',
    'WAESP32AU1V010FIFNoNlpNoMul', 'WAESP32AU1V010FIFNoNlpNoMulNoHpm'
]

for i, (instr, label) in enumerate(zip(configs, labels)):
    ax.bar(index + i * bar_width, instr, bar_width, label=label)

ax.set_xlabel('Benchmarks')
ax.set_ylabel('Nombre d\'instructions')
ax.set_title('Nombre d\'instructions par benchmark et configuration')
ax.set_xticks(index + bar_width * num_configs / 2 - bar_width / 2)
ax.set_xticklabels(benchmarks, rotation=90)
ax.legend()

ax.set_ylim(0, 80e6)
plt.tight_layout()  # Ajuster automatiquement la disposition pour éviter le chevauchement
plt.show()
