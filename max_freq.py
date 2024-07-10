import matplotlib.pyplot as plt

# Configuration names
configurations = [
    "WAESP32AU1V010", "WAESP32AU1V010M", "WAESP32AU1V010IF1", "WAESP32AU1V010JAlBr",
    "WAESP32AU1V010F", "WAESP32AU1V010IF1", "WAESP32AU1V010FIF", "WAESP32AU1V010FIFJalBr",
    "WAESP32AU1V010JalBr2", "WAESP32AU1V010NoNlp", "WAESP32AU1V010FIFNoNlp",
    "WAESP32AU1V010FIFNoNlpNoMul", "WAESP32AU1V010FIFNoNlpNoHpm",
    "WAESP32AU1V010FIFNoNlpNoMulNoHpm", "WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2", "WAESP32AU1V010FIFNoNlpNoHpmMulReg",
    "WAESP32AU1V011", "WAESP32AU1V030"
]

# Maximum frequencies for each configuration
frequencies = [
    58, 77, 82, 61, 78, 82, 72, 61, 61, 75, 76, 83, 70, 99, 90, 84, 56, 59
]

# Creating the bar chart
plt.figure(figsize=(10, 8))
plt.barh(configurations, frequencies, color='skyblue')
plt.xlabel('Fréquence maximale (MHz)')
plt.title('Fréquence maximale par configuration')
plt.gca().invert_yaxis()  # Invert y-axis to show the first entry at the top
plt.tight_layout()

# Show the plot
plt.show()