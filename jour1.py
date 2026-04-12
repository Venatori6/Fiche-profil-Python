def creerProfil(prenom, age, ville, langages):
    return {
        "prenom": prenom,
        "age": age,
        "ville": ville,
        "langages": langages
    }

def afficherProfil(profil):
    print("--- Fiche Profil ---")
    print(f"Nom    : {profil['prenom']}")
    print(f"Age    : {profil['age']} ans")
    print(f"Ville  : {profil['ville']}")
    print(f"Statut : {analyser_age(profil)}")
    print(f"Niveau : {analyserNiveau(profil)}")
    print("Langages :")
    for index, langage in enumerate(profil["langages"]):
        print(f"  {index + 1}. {langage}")

def analyserNiveau(profil):
    if len(profil["langages"]) >= 4:
        return "Développeur confirmé"
    elif len(profil["langages"]) >= 2:
        return "Développeur débutant"
    else:
        return "Débutant"
def analyser_age(profil):
    if profil["age"] >= 18:
        return "Majeur"
    elif profil["age"] >= 13:
        return "Ado"
    else:
        return "Enfant"    

print("=== Création de ta fiche profil ===")
prenom = input("Ton prénom : ")
age = int(input("Ton âge : "))
ville = input("Ta ville : ")

langages = []
print("Tes langages (tape 'stop' pour terminer) :")
while True:
    langage = input("- ")
    if langage == "stop":
        break
    langages.append(langage)

profil = creerProfil(prenom, age, ville, langages)
afficherProfil(profil)
analyser_age(profil)