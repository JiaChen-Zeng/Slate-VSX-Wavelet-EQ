import csv

# Read the CSV file
with open('eq_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the first line
    data = list(reader)

# Write to AutoEQ format
with open('autoeq_format.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Frequency', 'Amplitude'])
    for row in data:
        frequency = row[0]
        amplitude = row[1]
        writer.writerow([frequency, amplitude])
