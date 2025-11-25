nbConvives=int(input("Entrez le nombre de personne(s) conviées à la fondue:"))
base=4
fromage= (800 * nbConvives/ base)
eau= (2 * nbConvives/ base)
ail= (2* nbConvives/ base)
pain= (400 * nbConvives/ base)
print(f"Pour faire une fondue fribourgeoise pour 3 persones, ils vous faut: {fromage} gr de fromage {eau} dl d'eau {ail} gousse(s) d'ail {pain} gr de pain")
