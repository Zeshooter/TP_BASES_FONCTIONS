import csv
import os

# os.mkdir("adherents")
repertoire=os.listdir("C:/Users/Ulrich 2/Documents/Adrar/TP_BASES_FONCTIONS/TP_BASES_FONCTIONS/adherents/")
print(repertoire)
for i in repertoire:
    with open(i,"r") as fichier_csv:
        lire=csv.reader(fichier_csv)
        print (lire)

# with open("inscrits"+*+"-"+*+"-"+*+".csv","r") as file :
#     lecture=csv.reader(file)
#     for row in lecture:
#         print(row)