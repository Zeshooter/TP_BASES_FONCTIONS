import csv
import os

with open("C:/Users/Ulrich 2/Documents/Adrar/TP_BASES_FONCTIONS/TP_BASES_FONCTIONS/adherents/inscrits12-01-22.csv","r") as fichier_csv:
    lire=csv.reader(fichier_csv)
    for ligne in lire:
        print(ligne)


# repertoire=os.listdir("C:/Users/Ulrich 2/Documents/Adrar/TP_BASES_FONCTIONS/TP_BASES_FONCTIONS/adherents/")
# print(repertoire)
# for i in repertoire:
#     with open(i,"r") as fichier_csv:
#         lire=csv.reader(fichier_csv)
#         print (lire)