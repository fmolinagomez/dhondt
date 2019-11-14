#!/usr/bin/env python3

import dhondt
import csv

def main ():
    data =open('provincias.csv', encoding = 'utf=8')
    reader = csv.reader(data, delimiter=";")
#    for col in reader:
#        print(col)
    votos = {}
    for row in reader:
        key = row[0]
        votos[key] = int(row[1])


    result = dhondt.dhondt(350,0.0001,votos)
    print(result)
    print('<seats: {0}>'.format(sorted(result.repre.items(), key=lambda p: p[1], reverse=True)))

if __name__ == '__main__':
    main()
