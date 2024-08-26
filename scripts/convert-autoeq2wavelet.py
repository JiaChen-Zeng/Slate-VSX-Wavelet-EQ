import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

# Load your measurement data
measurement_data = pd.read_csv('autoeq_format.csv', skiprows=1, header=None)
measurement_data.columns = ['Frequency', 'Amplitude']

# Define the target frequencies for Wavelet
target_frequencies = np.array([
    20, 21, 22, 23, 24, 26, 27, 29, 30, 32, 34, 36, 38, 40, 43, 45, 48, 50, 53, 56, 59, 63, 66, 70, 74, 78, 83, 87, 92, 97, 
    103, 109, 115, 121, 128, 136, 143, 151, 160, 169, 178, 188, 199, 210, 222, 235, 248, 262, 277, 292, 309, 326, 345, 364, 
    385, 406, 429, 453, 479, 506, 534, 565, 596, 630, 665, 703, 743, 784, 829, 875, 924, 977, 1032, 1090, 1151, 1216, 1284, 
    1357, 1433, 1514, 1599, 1689, 1784, 1885, 1991, 2103, 2221, 2347, 2479, 2618, 2766, 2921, 3086, 3260, 3443, 3637, 3842, 
    4058, 4287, 4528, 4783, 5052, 5337, 5637, 5955, 6290, 6644, 7018, 7414, 7831, 8272, 8738, 9230, 9749, 10298, 10878, 
    11490, 12137, 12821, 13543, 14305, 15110, 15961, 16860, 17809, 18812, 19871
])

# Interpolate the measurement data to match the target frequencies
interpolation_function = interp1d(measurement_data['Frequency'], measurement_data['Amplitude'], kind='cubic', fill_value="extrapolate")
interpolated_amplitudes = interpolation_function(target_frequencies)

# Create the Wavelet format string
wavelet_format = "GraphicEQ: " + "; ".join(f"{freq} {amp:.2f}" for freq, amp in zip(target_frequencies, interpolated_amplitudes))

# Save to a text file
with open('wavelet_data.txt', 'w') as file:
    file.write(wavelet_format)

print("Wavelet format data generated successfully.")
