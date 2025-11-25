y=int(input("entrez un nombre entier:"))






if y==0:
    print(f"le nombre est zéro et il est pair")
else:
    if y > 0:
        signe = "positif"

    else:
        signe = "negatif"

    if y % 2 ==0:
        parite = "pair"
    else:
        parite = "impair"
    print(f"Le nombre est {signe} et {parite}")