import matplotlib.pyplot as plt
import numpy as np

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
                                          2.445, 2.435],
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
    "WAESP32AU1V010NoHpm2Btb8": [1.187, 1.274, 1.565, 1.434, 1.631, 1.749, 1.131, 1.754, 1.532, 1.048,
                                 1.071, 3.319, 1.310, 2.205, 1.471, 1.871, 1.803, 1.627, 1.679, 1.801,
                                 1.885, 1.697],
    "WAESP32AU1V010NoHpm2Btb16IFReg": [1.915, 1.773, 2.161, 1.557, 2.202, 1.816, 1.968, 2.557, 2.311, 1.566,
                                       1.568, 3.697, 1.807, 2.843, 1.867, 2.443, 2.511, 2.311, 2.025, 2.392,
                                       2.564, 2.411],
    "WAESP32AU1V010NoHpm2Btb8IFReg": [1.915, 1.773, 2.161, 1.557, 2.202, 1.816, 1.968, 2.557, 2.311, 1.566,
                                      1.568, 3.697, 1.807, 2.843, 1.867, 2.443, 2.511, 2.311, 2.025, 2.392,
                                      2.564, 2.411]
}

# Calculating the average CPI for each benchmark across all configurations
cpi_mean = np.mean(list(configs.values()), axis=0)

# Calculating percentage differences from the average
percent_diff = {label: (np.array(cpi) - cpi_mean) / cpi_mean * 100 for label, cpi in configs.items()}

# Number of configurations and benchmarks
num_configs = len(configs)
index = np.arange(len(benchmarks))
bar_width = 0.7 / num_configs  # Adjusting the width of the bars

# Creating the plot
fig, ax = plt.subplots(figsize=(20, 10))

# Plotting the bars for each configuration
for i, (label, cpi) in enumerate(configs.items()):
    bars = ax.bar(index + i * bar_width, cpi, bar_width, label=label)
    
    # Adding percentage labels above the bars
    for j, bar in enumerate(bars):
        height = bar.get_height()
        ax.annotate(f'{percent_diff[label][j]:.1f}%',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # Offset in pixels
                    textcoords="offset points",
                    ha='center', va='bottom',
                    rotation=90, fontsize=8)  # Font size and rotation for better readability

# Customizing the axes and title
ax.set_xlabel('Nom du benchmark')
ax.set_ylabel('CPI')
ax.set_title('Comparaison de CPI par programme et configuration')
ax.set_xticks(index + bar_width * num_configs / 2 - bar_width / 2)
ax.set_xticklabels(benchmarks, rotation=90)

# Adding a legend
ax.legend(title="Configurations", bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjusting the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()
