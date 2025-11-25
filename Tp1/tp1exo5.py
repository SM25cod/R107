print("Aujourd'hui est quel jour?")
      jour = int(input())
print("Quel heure est t'il?")
      heure = int(input())
print("Combien de minutes se sont écoulés?")
      minute = int(input())

Vjour= jour - 1

res1= (Vjour*24)*60
res2= heure*60
res3 = minute

ResultatF = res1 + res2 + res3
print (ResultatF)
