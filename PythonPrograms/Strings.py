import csv
f=open('data.csv')
csv_f=csv.reader(f)
for row in csv_f:
    print((row[1]))
f.close()