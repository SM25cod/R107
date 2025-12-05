l=[]

n=float(input("Vous cherchez la table de multiplication de quel nombre?"))
for i in range(10):
    p=i*n
    l.append(round(p,2))
    print(p)

for i in range(len(l)):
    print(f"{n} * {i} = {l[i]}")

