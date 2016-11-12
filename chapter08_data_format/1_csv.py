import csv

with open('sample.csv', mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open('sample.csv', mode='a', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['6', '민정희', '85', '80.6'])

with open('sample.csv', mode='r', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        print(row)
