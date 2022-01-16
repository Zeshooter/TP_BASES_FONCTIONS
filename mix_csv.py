import csv
import os

adherent=[]
# os.mkdir("adherents")

# recherche des fichier csv
repertoire=os.listdir("C:/Users/Ulrich 2/Documents/Adrar/TP_BASES_FONCTIONS/TP_BASES_FONCTIONS/")
print(repertoire)

# lecture des tuples dans les fichiers csv et stockage dans la liste adherent
for i in repertoire:
    if ".csv" in i:
        with open(i,"r") as fichier_csv:
            lire=csv.reader(fichier_csv)
            for ligne in lire:
                adherent.append(ligne)
                print (adherent)

# ecriture des tuples dans un fichier
with open("C:/Users/Ulrich 2/Documents/Adrar/TP_BASES_FONCTIONS/TP_BASES_FONCTIONS/adherents/inscrits_total.csv", "a") as fichier_csv:
    writer=csv.writer(fichier_csv, delimiter=";", lineterminator="\n")
    for row in adherent:
        writer.writerow(row)
print("Un nouveau fichier a été crée avec tous les adhérents")


