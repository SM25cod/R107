hd=int(input("Donnez l'heure de début de la location (un entier):"))
hf=int(input("Donnez l'heure de fin de la location (un entier):"))
cmpt1=0
cmpt2=0
somme=0
while hd < 0 or hf < 0 or hd > 24 or hf > 24 or hd == hf or hf < hf:
    if hd < 0 or hf < 0 or hd > 24 or hf > 24:
        print("Les heures doivent être comprises entre 0 et 24")
    if hd == hf:
        print("Attention ! l’heure de fin est identique à l’heure de début")
    if hf < hf:
        print("Attention ! le début de la location est après la fin ...")

    hd=int(input("Donnez l'heure de début de la location (un entier):"))
    hf=int(input("Donnez l'heure de fin de la location (un entier):"))

for i in range(hd,hf):
    if 0<= i <7 or 17<i<24:
        cmpt1+=1
    else:
        cmpt2+=1

somme=cmpt1+2*cmpt2
print(f"Le montant total à payer est de {somme} euro(s).")