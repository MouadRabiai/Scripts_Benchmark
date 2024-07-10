import matplotlib.pyplot as plt
import numpy as np


benchmarks = [
    "aha-mont64", "crc32", "cubic", "edn", "huffbench", 
    "matmult-int", "md5sum", "minver", "nbody", "nettle-aes",
    "nettle-sha256", "nsichneu", "picojpeg", "primecount", 
    "qrduino", "sglib-combined", "slre", "st", "statemate", 
    "tarfind", "ud", "wikisort"
]


cpi_WAESP32AU1V010 = [1.102, 1.136, 1.430, 1.297, 1.379, 1.280, 1.045, 1.630, 1.383, 1.035, 1.049, 2.785, 1.232, 1.751, 1.412, 1.628, 1.671, 1.570, 1.604, 1.728, 1.551, 1.553]
cpi_WAESP32AU1V010M = [1.184, 1.061, 1.440, 1.179, 1.301, 1.417, 1.046, 1.436, 1.422, 1.058, 1.044, 2.786, 1.129, 1.595, 1.384, 1.550, 1.593, 1.431, 1.432, 1.326, 1.516, 1.365]
cpi_WAESP32AU1V010IF1 = [1.972, 1.727, 2.556, 2.792, 2.084, 2.624, 1.855, 2.591, 2.584, 1.691, 1.572, 3.712, 1.967, 2.778, 2.309, 2.459, 2.457, 2.580, 2.611, 2.605, 2.531, 2.492]
cpi_WAESP32AU1V010JalBr = [1.762, 1.500, 2.090, 1.742, 1.654, 2.098, 1.527, 2.060, 2.065, 1.556, 1.522, 2.847, 1.507, 2.170, 1.868, 1.926, 1.912, 2.071, 1.753, 1.949, 2.182, 1.958]
cpi_WAESP32AU1V010F = [1.762, 1.500, 2.090, 1.742, 1.654, 2.098, 1.527, 2.060, 2.065, 1.556, 1.522, 2.847, 1.507, 2.170, 1.868, 1.926, 1.912, 2.071, 1.753, 1.949, 2.182, 1.958]
cpi_WAESP32AU1V010FIF = [1.825, 1.955, 2.060, 1.520, 2.143, 2.092, 1.856, 2.420, 2.133, 1.552, 1.546, 3.164, 1.722, 2.448, 1.722, 2.199, 2.272, 2.191, 1.856, 2.432, 2.261, 2.254]
cpi_WAESP32AU1V010FIFJalBr = [1.638, 1.501, 1.912, 1.307, 1.654, 1.570, 1.527, 2.184, 1.909, 1.504, 1.522, 2.848, 1.470, 2.099, 1.561, 1.907, 1.906, 2.023, 1.754, 2.063, 2.027, 2.011]
cpi_WAESP32AU1V010FIFNoNlp = [1.966, 2.227, 2.089, 1.786, 2.360, 2.126, 2.049, 2.434, 2.202, 1.552, 1.551, 3.164, 1.846, 2.912, 1.869, 2.430, 2.350, 2.200, 1.864, 2.884, 2.282, 2.426]
cpi_WAESP32AU1V010FIFNoNlpNoMul = [2.926, 2.000, 2.926, 3.263, 2.360, 3.287, 2.049, 2.860, 3.010, 1.660, 1.551, 3.164, 1.894, 3.159, 2.490, 2.484, 2.350, 2.956, 1.864, 2.803, 2.874, 2.780]
cpi_WAESP32AU1V010FIFNoNlpNoMulNoHpm = [2.218, 2.000, 2.926, 3.263, 2.360, 3.287, 2.049, 2.860, 3.010, 1.660, 1.551, 3.164, 1.894, 3.159, 2.490, 2.484, 2.350, 2.956, 1.864, 2.803, 2.874, 2.780]



num_configs = 10


index = np.arange(len(benchmarks))
bar_width = 0.08  

fig, ax = plt.subplots(figsize=(20, 10))  


offset = 0
configs = [cpi_WAESP32AU1V010, cpi_WAESP32AU1V010M, cpi_WAESP32AU1V010IF1, cpi_WAESP32AU1V010JalBr, cpi_WAESP32AU1V010F, cpi_WAESP32AU1V010FIF, cpi_WAESP32AU1V010FIFJalBr, cpi_WAESP32AU1V010FIFNoNlp, cpi_WAESP32AU1V010FIFNoNlpNoMul, cpi_WAESP32AU1V010FIFNoNlpNoMulNoHpm]
labels = ['WAESP32AU1V010', 'WAESP32AU1V010M', 'WAESP32AU1V010IF1', 'WAESP32AU1V010JalBr', 'WAESP32AU1V010F', 'WAESP32AU1V010FIF', 'WAESP32AU1V010FIFJalBr', 'WAESP32AU1V010FIFNoNlp', 'WAESP32AU1V010FIFNoNlpNoMul', 'WAESP32AU1V010FIFNoNlpNoMulNoHpm']

for i, (cpi, label) in enumerate(zip(configs, labels)):
    ax.bar(index + i * bar_width, cpi, bar_width, label=label)

ax.set_xlabel('EXEC NAME')
ax.set_ylabel('CPI')
ax.set_title('CPI par programme et configuration')
ax.set_xticks(index + bar_width * num_configs / 2 - bar_width / 2)
ax.set_xticklabels(benchmarks, rotation=90)
ax.legend()

plt.tight_layout()  
plt.show()
