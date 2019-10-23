##print("CODIGO    ESPECIFICAÇÃO    PREÇO")
##print("1         Cachorro Quente  R$4.00")
##print("2         X-Salada         R$4.50")
##print("3         X-Bacon          R$5.00")
##print("4         Torrada Simples  R$2.00")
##print("5         Refrigerante     R$1.50")
Codigo, Quantidadeitem = str(input()).split()
Codigo = int(Codigo)
Quantidadeitem = int(Quantidadeitem)
# Condições Para Decidir A Opção
if(Codigo == 1):
    Compra = Quantidadeitem * 4.00
elif(Codigo == 2):
    Compra = Quantidadeitem * 4.50
elif(Codigo == 3):
    Compra = Quantidadeitem * 5.00
elif(Codigo == 4):
    Compra = Quantidadeitem * 2.00
elif(Codigo == 5):
    Compra = Quantidadeitem * 1.50
print("Total: R$ {:.2f}".format(Compra))

