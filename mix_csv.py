import csv
import os


with open("inscrits"+*+"-"+*+"-"+*+".csv","r") as file :
    lecture=csv.reader(file)
    for row in lecture:
        print(row)