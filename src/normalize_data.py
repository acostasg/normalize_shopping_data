import csv

dataset = []
with open('../input/dataset.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0])
        for value in row
            dataset.append(row)
