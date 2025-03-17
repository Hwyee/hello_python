""" csv_file.py"""
import csv

with open("data.csv", "w+", encoding="utf-8") as f:
    cw = csv.writer(f)
    cw.writerow(["a", "b", "c"])
    cw.writerow(["1", "2", "3"])
    cw.writerows([["4", "5", "6"], ["7", "8", "9"]])

with open("data.csv", "r+", encoding="utf-8") as f:
    rd = csv.reader(f)
    for row in rd:
        print(row)
