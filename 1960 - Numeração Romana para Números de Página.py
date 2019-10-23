n = int(input())
if(n > 0 and n < 1000):
    n = str(n)

    # Centena - Centena

    if(len(n) == 3):

        if(int(n[0]) > 5):
            if (int(n[0]) == 9):
                r = "CM"
            else:
                r = "D" + ("C")*(int(n[0])-5)

        elif(int(n[0]) == 5):
            r = "D"

        elif(int(n[0]) < 5):
            if(int(n[0]) == 4):
                r = "CD"
                
            else:
                r = "C"*int(n[0])
        # Dezena - Centena

        if(int(n[1]) > 5):
            if (int(n[1]) == 9):
                r = r + "XC"
            else:
                r = r + "L" + ("X")*(int(n[1])-5)

        elif(int(n[1]) == 5):
            r = r + "L"

        elif(int(n[1]) < 5):
            if(int(n[1]) == 4):
                r = r + "XL"
                
            else:
                r = r + "X"*int(n[1])

        # Unidade -Centena
        if(int(n[2]) > 5):
            if (int(n[2]) == 9):
                r = r + "IX"
            else:
                r = r + "V" + ("I")*(int(n[2])-5)

        elif(int(n[2]) == 5):
            r = r + "V"

        elif(int(n[2]) < 5):
            if(int(n[2]) == 4):
                r = r + "IV"
                
            else:
                r = r + "I"*int(n[2])

    # Dezena - Dezena
    if(len(n) == 2):

        if(int(n[0]) > 5):
            if (int(n[0]) == 9):
                r = "XC"
            else:
                r = "L" + "X"*(int(n[0])-5)

        elif(int(n[0]) == 5):
            r = "L"

        elif(int(n[0]) < 5):
            if(int(n[0]) == 4):
                r = "XL"
                    
            else:
                r = "X"*int(n[0])

            # Unidade - Dezena
        if(int(n[1]) > 5):
            if (int(n[1]) == 9):
                r = r + "IX"
            else:
                r = r + "V" + ("I")*(int(n[1])-5)

        elif(int(n[1]) == 5):
            r = r + "V"

        elif(int(n[1]) < 5):
            if(int(n[1]) == 4):
                r = r + "IV"
                
            else:
                r = r + "I"*int(n[1])
                    
    # unidades - Unidade
    if(len(n) == 1):
                    
        if(int(n[0]) > 5):
            if (int(n[0]) == 9):
                r = "IX"
            else:
                r = "V" + ("I")*(int(n[0])-5)

        elif(int(n[0]) == 5):
            r = "V"

        elif(int(n[0]) < 5):
            if(int(n[0]) == 4):
                r = "IV"                
            else:
                r = "I"*int(n[0])



    print(r)
