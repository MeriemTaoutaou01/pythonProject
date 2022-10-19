import math
p=10**3
V1=input("introduire valeur de vitesse 1: ")
D1=input("intrduire valeur du diamètre 1 en mètre: ")
MV=input("introduire la valeur de la masse volumique: ")
try:
    V1=float(V1)
    D1=float(D1)
    MV=float(MV)
    V2=V1*1.5
    D2=math.sqrt(D1**2/1.5)
    Ang=math.tan(10*3.14/180)
    L=(D1*(1-math.sqrt(V1/V2)))/(2*Ang)
    L1=L*1000
    VarP=(V2**2-V1**2)*MV/2
    print("la longuer du convergent est:",L1,"mm")
    print("la variation de la pression est:",VarP,"Pa")
except:
    print("une ou plusieurs valeurs intrduites sont incorrectes")



