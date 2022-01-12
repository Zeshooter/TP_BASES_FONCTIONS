import csv
import os

adherent=[]
# os.mkdir("adherents")
repertoire=os.listdir("C:/Users/Ulrich 2/Documents/Adrar/TP_BASES_FONCTIONS/TP_BASES_FONCTIONS/")
print(repertoire)
for i in repertoire:
    if ".csv" in i:
        with open(i,"r") as fichier_csv:
            lire=csv.reader(fichier_csv)
            for ligne in lire:
                adherent.append(ligne)
                print (adherent)

with open("C:/Users/Ulrich 2/Documents/Adrar/TP_BASES_FONCTIONS/TP_BASES_FONCTIONS/adherents/adherents.csv", "a") as fichier_csv:
    writer=csv.writer(fichier_csv)
    for row in adherent:
        writer.writerow(row)

# with open("inscrits"+*+"-"+*+"-"+*+".csv","r") as file :
#     lecture=csv.reader(file)
#     for row in lecture:
#         print(row)