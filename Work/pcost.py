# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(file):
    'Read CSV file of stock, shares, price and compute total cost'
    f = open(file, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    total = 0
    for row in rows:
        try:
            stock, shares, price = row
            total = total + int(shares)*float(price)
        except ValueError: # handle missing values
            print("Couldn't parse", row)
    f.close()
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

total = portfolio_cost(filename)
print(f"Total cost {total:.2f}")
