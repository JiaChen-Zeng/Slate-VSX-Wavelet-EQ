import csv

# Read the CSV file
with open('eq_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

# Write to AutoEQ format
with open('autoeq_format.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Frequency', 'Gain'])
    for row in data:
        frequency = row[0]
        gain = row[1]
        writer.writerow([frequency, gain])
