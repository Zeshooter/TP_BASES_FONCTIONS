# import des fonctions de calculs
import fonctions

# Saisie des données dans une liste

nom_adherents=[]
prenom_adherents=[]
categorie=["Poussin","Cadet","Junior","Semi-Pro","Pro"]
categorie_adherents=[]
adherents=[]

saisie=False
while saisie==False:
    try:
        nbre_adherent=int(input("Combien d'adhérent voulez vous saisir ?\n"))
        saisie=True
    except ValueError:
        print("Vous devez entrer un nombre entier ?")

for i in range(nbre_adherent):
    nom_adherents.append(input("Nom de l'adhérent ?\n"))
    prenom_adherents.append(input("prenom de l'adherent?\n"))

    # Vérification de l'admission de l'adhérent
    saisie=False
    while saisie==False:
        try:
            anneenaissance=int(input("Veuillez Indiquer l'année de naissance de l'adhérent ?\n"))
            saisie=True
        except ValueError:
            print("Vous devez entrér l'année en chiffre")

    age_adherent=fonctions.age_adherent(anneenaissance)

    if age_adherent >6 and age_adherent <12:
        print("l'adhérent est dans la catégorie Poussin")
        categorie_adherents.append("Poussin")
    elif age_adherent >=12 and age_adherent <18:
        print("l'adhérent est dans la catégorie Cadet")
        categorie_adherents.append("Cadet")
    elif age_adherent >=18 and age_adherent <24:
        print("l'adhérent est dans la catégorie Junior")
        categorie_adherents.append("Junior")
    elif age_adherent >=24 and age_adherent <30:
        print("l'adhérent est dans la catégorie Semi-Pro")
        categorie_adherents.append("Semi-Pro")
    elif age_adherent >=30 and age_adherent <40:
        print("l'adhérent est dans la catégorie Pro")
        categorie_adherents.append("Pro")
    else:
        nom_adherents.pop(0)
        prenom_adherents.pop(0)
        print("L'adhérent n'a pas l'âge requis pour intégrer le club de quidditch !")


    # Enregistrement de l'adhérent dans une liste + création de l'email

    if nom_adherents:
        adherents.append((nom_adherents[0],prenom_adherents[0],categorie_adherents[0],(prenom_adherents[0][0])+"."+(nom_adherents[0])+"@baton-rouge.fr"))
        nom_adherents.pop(0)
        prenom_adherents.pop(0)
        categorie_adherents.pop(0)
    else:
        print("Cette personne ne peut pas adhérer au club de Quidditch car ici on discrimine les jeunes et les vieux !!!")



print(nom_adherents, prenom_adherents, categorie_adherents, adherents)



