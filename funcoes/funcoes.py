c = [800, 500, 350, 200]  
g = [1500, 600, 2400]      

def somatorio(lista):
    return sum(lista)

d = somatorio(g) - somatorio(c)

print(f"Custos: R${sum(c)}")
print(f"Ganhos: R${sum(g)}")
print(f"Diferença: R${d}")