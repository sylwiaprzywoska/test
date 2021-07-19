do_3_potegi = []
podzielne_przez_5 = []
for i in range (0, 101):
    if (i % 5 == 0):
        podzielne_przez_5.append(i)
        do_3_potegi.append(i**3)
print(podzielne_przez_5)
print(do_3_potegi)