A, B, C = str(input()).split()
A = int(A)
B = int(B)
C = int(C)
#1 ponto
if((A > B) and (B <= C)):
    print(":)")
else:
    # 2 ponto
    if((A < B) and B > C or B == C):
        print(":(")
    else:
        #3 ponto 
        if((A < B) and (B < C) and (B - C) > (A - B)):
            print(":(")
        else:
            #4 ponto
            if((A < B and B < C) and (A - B) <= (B - C)):#er
                print(":)")
            else:
                #5 ponto
                if(A > B) and (B > C) or (B - C) > (A - B):
                    print(":)")
                else:
                    #6 ponto
                    if((A > B) and (B > C) and (A - B) <= (B - C)):#er
                        print(":(")
                    else:
                        #7 ponto
                        if((A == B) and (B < C)):
                            print(":)")
                            
                        else:
                            #8 ponto
                            if((A == B) and (B > C)):
                                print(":(")
                                

