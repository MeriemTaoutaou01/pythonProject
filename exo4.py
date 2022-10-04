e1=input("Entrer la valeur de la masse volumique du platine: ")
e2=input("Entrer la valeur de la masse volumique du zinc: ")
e=input("saisir la valeur de la masse volumique du fluide: ")
try:
    e1=float(e1)
    e2=float(e2)
    e=float(e)
    min=(e1-e)//(e-e2)
    print("La valeur minimale pour que le solide puisse flotter est:",min,)
except:
    input("L'une des valeurs saisies n'est pas correste")