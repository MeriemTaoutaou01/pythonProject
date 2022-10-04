g=9.8
e=input("saisir la valeur de masse volumique du fluide: ")
pr=input("saisir la valeur de profondeur: ")
l=input("entrer la valeur de la largeur du barrage: ")
try:
    e=float(e)
    pr=float(pr)
    l=float(l)
    p=pr*e*g
    f=p*l*pr
    print("la pression en bas du barrage est:",p,"Pa")
    print("la force exercée par l'eau est:",f,"N")
except:
    print("l'une des valeurs saisies n'est pas correcte")
