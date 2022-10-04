d=input("Entrer la valeur de diamètre: ")
p=6.9*10**(6)
try:
    d=float(d)
    s=2*3.14*(d//2)**2
    f=p*s
    print("La valeur de la force est:",f,"N")
except:
    print("la valeur de d n'est pas correcte")