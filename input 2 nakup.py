def nakup(zoznam):
    cena=0
    for i in range(0,len(zoznam),2): #start, stop, step
        cena+=zoznam[i] * zoznam[i+1] #ks*cena
    return cena

print(nakup([3, 2.5, 0.5, 10, 1.2, 1.2]))
print(nakup([4, 12, 0.3, 15, 22, 1]))

