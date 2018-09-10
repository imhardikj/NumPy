import csv
with open('winequality-red.csv', 'r') as f:
    wines = list(csv.reader(f, delimiter=';'))
quality = [float(item[-1]) for item in wines[1:]]

print(sum(quality)/len(quality))