Tipo = str(input()).lower()
Classe = str(input()).lower()
Talimentação = str(input()).lower()

if(Tipo == "vertebrado" and Classe == "ave" and Talimentação == "carnivoro"):
    print("aguia")
elif(Tipo == "vertebrado" and Classe == "ave" and Talimentação == "onivoro"):
    print("pomba")
elif(Tipo == "vertebrado" and Classe == "mamifero" and Talimentação == "onivoro"):
    print("homem")
elif(Tipo == "vertebrado" and Classe == "mamifero" and Talimentação == "herbivoro"):
    print("vaca")
elif(Tipo == "invertebrado" and Classe == "inseto" and Talimentação == "hematofago"):
    print("pulga")
elif(Tipo == "invertebrado" and Classe == "inseto" and Talimentação == "herbivoro"):
    print("lagarta")
elif(Tipo == "invertebrado" and Classe == "anelideo" and Talimentação == "hematofago"):
    print("sanguessuga")
elif(Tipo == "invertebrado" and Classe == "anelideo" and Talimentação == "onivoro"):
    print("minhoca")
