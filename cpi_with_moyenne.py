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

# Définir les CPI pour chaque configuration
cpi_WAESP32AU1V010 = [1.102, 1.136, 1.430, 1.297, 1.379, 1.280, 1.045, 1.630, 1.383, 1.035, 1.049, 2.785, 1.232, 1.751, 1.412, 1.628, 1.671, 1.570, 1.604, 1.728, 1.551, 1.553]
cpi_WAESP32AU1V010JalBr = [1.762, 1.500, 2.090, 1.742, 1.654, 2.098, 1.527, 2.060, 2.065, 1.556, 1.522, 2.847, 1.507, 2.170, 1.868, 1.926, 1.912, 2.071, 1.753, 1.949, 2.182, 1.958]
cpi_WAESP32AU1V010F = [1.762, 1.500, 2.090, 1.742, 1.654, 2.098, 1.527, 2.060, 2.065, 1.556, 1.522, 2.847, 1.507, 2.170, 1.868, 1.926, 1.912, 2.071, 1.753, 1.949, 2.182, 1.958]
cpi_WAESP32AU1V010FIF = [1.825, 1.955, 2.060, 1.520, 2.143, 2.092, 1.856, 2.420, 2.133, 1.552, 1.546, 3.164, 1.722, 2.448, 1.722, 2.199, 2.272, 2.191, 1.856, 2.432, 2.261, 2.254]
cpi_WAESP32AU1V010FIFJalBr = [1.638, 1.501, 1.912, 1.307, 1.654, 1.570, 1.527, 2.184, 1.909, 1.504, 1.522, 2.848, 1.470, 2.099, 1.561, 1.907, 1.906, 2.023, 1.754, 2.063, 2.027, 2.011]
cpi_WAESP32AU1V010FIFNoNlp = [1.966, 2.227, 2.089, 1.786, 2.360, 2.126, 2.049, 2.434, 2.202, 1.552, 1.551, 3.164, 1.846, 2.912, 1.869, 2.430, 2.350, 2.200, 1.864, 2.884, 2.282, 2.426]


configs = [cpi_WAESP32AU1V010, cpi_WAESP32AU1V010JalBr, cpi_WAESP32AU1V010F, cpi_WAESP32AU1V010FIF, cpi_WAESP32AU1V010FIFJalBr, cpi_WAESP32AU1V010FIFNoNlp]
labels = ['WAESP32AU1V010', 'WAESP32AU1V010JalBr', 'WAESP32AU1V010F', 'WAESP32AU1V010FIF', 'WAESP32AU1V010FIFJalBr', 'WAESP32AU1V010FIFNoNlp']


num_benchmarks = len(benchmarks)
num_configs = len(configs)


cpi_mean = np.mean(configs, axis=0)


percent_diff = [(np.array(cpi) - cpi_mean) / cpi_mean * 100 for cpi in configs]


index = np.arange(num_benchmarks)
bar_width = 0.12  

fig, ax = plt.subplots(figsize=(20, 10)) 

for i, (cpi, label) in enumerate(zip(configs, labels)):
    bars = ax.bar(index + i * bar_width, cpi, bar_width, label=label)
    
   
    for j, bar in enumerate(bars):
        height = bar.get_height()
        percentage = percent_diff[i][j]
        ax.annotate(f'{percentage:.1f}%',  
                    xy=(bar.get_x() + bar.get_width() / 2, height),  
                    xytext=(0, 3),  
                    textcoords="offset points",  
                    ha='center', va='bottom', fontsize=8, rotation=90, color='black') 


ax.set_xlabel('Benchmarks')
ax.set_ylabel('CPI')
ax.set_title('CPI par benchmark et configuration (avec pourcentage de décalage)')
ax.set_xticks(index + bar_width * num_configs / 2 - bar_width / 2)
ax.set_xticklabels(benchmarks, rotation=90)
ax.legend()

plt.tight_layout()  
plt.show()
