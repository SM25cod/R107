# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0;
# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = []

for i in range (nombreEtudiants):

    note = float(input(f"Merci de donnez la note de l'étudiant {i+1} : "))
    notes.append(note)
    moyenne = i

#print(f"{note}*{i}={moyenne}")
print(notes)
print(f" la moyenne est {moyenne}")