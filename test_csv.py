import csv
with open ('test.csv','w',newline='') as csvfile:
    ecrire=csv.writer(csvfile)
    ecrire.write("bonjour")