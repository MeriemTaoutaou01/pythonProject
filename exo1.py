d=input("Entrer la valeur de la densité: ")
v=input("Entrer la valeur de la viscosité cinématique: ")
try:
    d=float(d)
    v=float(v)
    µ=0.0001*1000*d
    print("la valeur de la viscosité dynamique est:",µ,"PI")
except:
    print("La valeur de v et/ou d n'est pas correcte")
