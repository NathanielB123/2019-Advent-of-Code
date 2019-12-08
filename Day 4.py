Min=264793
Max=803935
ValidPasswords=[]
for Password in range(Min,Max):
    Prev=0
    Valid=True
    for Num in str(Password):
        if int(Num)>=Prev:
            Prev=int(Num)
        else:
            Valid=False
            break
    if Valid:
        Prev=-1
        Valid=False
        for Num in str(Password):
            if Num==Prev:
                Valid=True
            Prev=Num
    if Valid:
        ValidPasswords.append(Password)
print(len(ValidPasswords))

# Part 2

ValidPasswords=[]
for Password in range(Min,Max):
    Prev=0
    Valid=True
    for Num in str(Password):
        if int(Num)>=Prev:
            Prev=int(Num)
        else:
            Valid=False
            break
    if Valid:
        Valid=False
        for NumNum in range(0,len(str(Password))-1):
            if str(Password)[NumNum]==str(Password)[NumNum+1]:
                if NumNum>0:
                    if NumNum<4:
                        if not(str(Password)[NumNum]==str(Password)[NumNum+2] or str(Password)[NumNum]==str(Password)[NumNum-1]):
                            Valid=True
                    else:
                        if not (str(Password)[NumNum]==str(Password)[NumNum-1]):
                            Valid=True
                else:
                    if not (str(Password)[NumNum]==str(Password)[NumNum+2]):
                        Valid=True
    if Valid:
        ValidPasswords.append(Password)
        print(Password)
print(len(ValidPasswords))
