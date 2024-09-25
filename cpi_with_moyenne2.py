import matplotlib.pyplot as plt
import numpy as np

# Benchmark names
benchmarks = [
    "aha-mont64", "crc32", "cubic", "edn", "huffbench",
    "matmult-int", "md5sum", "minver", "nbody", "nettle-aes",
    "nettle-sha256", "nsichneu", "picojpeg", "primecount",
    "qrduino", "sglib-combined", "slre", "st", "statemate",
    "tarfind", "ud", "wikisort"
]

# CPI data for each configuration
cpi_WAESP32AU1V010M = [1.184, 1.061, 1.440, 1.179, 1.301, 1.417, 1.046, 1.436, 1.422, 1.058, 1.044, 2.786, 1.129, 1.595, 1.384, 1.550, 1.593, 1.431, 1.432, 1.326, 1.516, 1.365]
cpi_WAESP32AU1V010IF1 = [1.972, 1.727, 2.556, 2.792, 2.084, 2.624, 1.855, 2.591, 2.584, 1.691, 1.572, 3.712, 1.967, 2.778, 2.309, 2.459, 2.457, 2.580, 2.611, 2.605, 2.531, 2.492]
cpi_WAESP32AU1V010JalBr = [1.762, 1.500, 2.090, 1.742, 1.654, 2.098, 1.527, 2.060, 2.065, 1.556, 1.522, 2.847, 1.507, 2.170, 1.868, 1.926, 1.912, 2.071, 1.753, 1.949, 2.182, 1.958]
cpi_WAESP32AU1V010FIFNoNlpNoMul = [2.926, 2.000, 2.926, 3.263, 2.360, 3.287, 2.049, 2.860, 3.010, 1.660, 1.551, 3.164, 1.894, 3.159, 2.490, 2.484, 2.350, 2.956, 1.864, 2.803, 2.874, 2.780]
cpi_WAESP32AU1V010FIFNoNlpNoMulNoHpm = [2.218, 2.000, 2.926, 3.263, 2.360, 3.287, 2.049, 2.860, 3.010, 1.660, 1.551, 3.164, 1.894, 3.159, 2.490, 2.484, 2.350, 2.956, 1.864, 2.803, 2.874, 2.780]

configs = [cpi_WAESP32AU1V010M, cpi_WAESP32AU1V010IF1, cpi_WAESP32AU1V010JalBr, cpi_WAESP32AU1V010FIFNoNlpNoMul, cpi_WAESP32AU1V010FIFNoNlpNoMulNoHpm]
labels = ['WAESP32AU1V010M', 'WAESP32AU1V010IF1', 'WAESP32AU1V010JalBr', 'WAESP32AU1V010FIFNoNlpNoMul', 'WAESP32AU1V010FIFNoNlpNoMulNoHpm']

# Calculating the average CPI for each benchmark across configurations
cpi_mean = np.mean(configs, axis=0)

# Calculating percentage differences from the average
percent_diff = [(np.array(cpi) - cpi_mean) / cpi_mean * 100 for cpi in configs]

# Number of configurations and benchmarks
num_configs = len(configs)
num_benchmarks = len(benchmarks)

# Plot settings
index = np.arange(num_benchmarks)
bar_width = 0.12

fig, ax = plt.subplots(figsize=(20, 10))

# Plotting the bars
for i, (cpi, label) in enumerate(zip(configs, labels)):
    bars = ax.bar(index + i * bar_width, cpi, bar_width, label=label)
    
    # Adding percentage labels above bars with a 90-degree rotation
    for j, bar in enumerate(bars):
        height = bar.get_height()
        ax.annotate(f'{percent_diff[i][j]:.1f}%', 
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # Offset in pixels
                    textcoords="offset points", 
                    ha='center', va='bottom',
                    rotation=90, fontsize=7)  # Rotate text to 90 degrees

# Labeling axes
ax.set_xlabel('Benchmarks')
ax.set_ylabel('CPI')
ax.set_title('CPI per Benchmark and Configuration')
ax.set_xticks(index + bar_width * num_configs / 2 - bar_width / 2)
ax.set_xticklabels(benchmarks, rotation=90)
ax.legend()

plt.tight_layout()
plt.show()
