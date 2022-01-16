import csv
import os

adherent=[]
# creation du repertoire
dir=os.listdir()
if "adherents" not in dir:
    os.mkdir("adherents")

# recherche des fichier csv
repertoire=os.listdir()

# lecture des tuples dans les fichiers csv et stockage dans la liste adherent
for i in repertoire:
    if ".csv" in i:
        with open(i,"r") as fichier_csv:
            lire=csv.reader(fichier_csv)
            for ligne in lire:
                adherent.append(ligne)


# dedoublonnage des tuple
new_list=[]
for i in adherent:
    if i not in new_list:
        new_list.append(i)
print (new_list)



# ecriture des tuples dans un fichier
with open("adherents/inscrits_total.csv", "w") as fichier_csv:
    writer=csv.writer(fichier_csv, delimiter=";", lineterminator="\n")
    for row in new_list:
        writer.writerow(row)
print("Un nouveau fichier a été crée avec tous les adhérents")

