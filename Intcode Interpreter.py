def RunIntcode(Code,Inputs,Index,RelativeBase):
    Running=True
    Returns=[]
    while Running and not int(str(Code[Index])[-2:])==99:
        Parameters=[]
        if int(str(Code[Index])[-2:])==1:
            if len(str(Code[Index]))<5:
                Parameters.append(Code[Index+3])
            elif int(str(Code[Index])[len(str(Code[Index]))-5])==0:
                Parameters.append(Code[Index+3])
            elif int(str(Code[Index])[len(str(Code[Index]))-5])==2:
                Parameters.append(Code[Index+3]+RelativeBase)
            else:
                Parameters.append(Index+3)
            if len(str(Code[Index]))<4:
                Parameters.append(Code[Index+2])
            elif int(str(Code[Index])[len(str(Code[Index]))-4])==0:
                Parameters.append(Code[Index+2])
            elif int(str(Code[Index])[len(str(Code[Index]))-4])==2:
                Parameters.append(Code[Index+2]+RelativeBase)
            else:
                Parameters.append(Index+2)
            if len(str(Code[Index]))<3:
                Parameters.append(Code[Index+1])
            elif int(str(Code[Index])[len(str(Code[Index]))-3])==0:
                Parameters.append(Code[Index+1])
            elif int(str(Code[Index])[len(str(Code[Index]))-3])==2:
                Parameters.append(Code[Index+1]+RelativeBase)
            else:
                Parameters.append(Index+1)
            Code[Parameters[0]]=Code[Parameters[1]]+Code[Parameters[2]]
            Index=Index+4
        elif int(str(Code[Index])[-2:])==2:
            if len(str(Code[Index]))<5:
                Parameters.append(Code[Index+3])
            elif int(str(Code[Index])[len(str(Code[Index]))-5])==0:
                Parameters.append(Code[Index+3])
            elif int(str(Code[Index])[len(str(Code[Index]))-5])==2:
                Parameters.append(Code[Index+3]+RelativeBase)
            else:
                Parameters.append(Index+3)
            if len(str(Code[Index]))<4:
                Parameters.append(Code[Index+2])
            elif int(str(Code[Index])[len(str(Code[Index]))-4])==0:
                Parameters.append(Code[Index+2])
            elif int(str(Code[Index])[len(str(Code[Index]))-4])==2:
                Parameters.append(Code[Index+2]+RelativeBase)
            else:
                Parameters.append(Index+2)
            if len(str(Code[Index]))<3:
                Parameters.append(Code[Index+1])
            elif int(str(Code[Index])[len(str(Code[Index]))-3])==0:
                Parameters.append(Code[Index+1])
            elif int(str(Code[Index])[len(str(Code[Index]))-3])==2:
                Parameters.append(Code[Index+1]+RelativeBase)
            else:
                Parameters.append(Index+1)
            Code[Parameters[0]]=Code[Parameters[1]]*Code[Parameters[2]]
            Index=Index+4
        elif int(str(Code[Index])[-2:])==3:
            if len(str(Code[Index]))<3:
                Parameters.append(Code[Index+1])
            elif int(str(Code[Index])[len(str(Code[Index]))-3])==0:
                Parameters.append(Code[Index+1])
            elif int(str(Code[Index])[len(str(Code[Index]))-3])==2:
                Parameters.append(Code[Index+1]+RelativeBase)
            else:
                Parameters.append(Index+1)
            Code[Parameters[0]]=Inputs[0]
            Inputs.pop(0)
            Index=Index+2
        elif int(str(Code[Index])[-2:])==4:
            if len(str(Code[Index]))<3:
                Parameters.append(Code[Index+1])
            elif int(str(Code[Index])[len(str(Code[Index]))-3])==0:
                Parameters.append(Code[Index+1])
            elif int(str(Code[Index])[len(str(Code[Index]))-3])==2:
                Parameters.append(Code[Index+1]+RelativeBase)
            else:
                Parameters.append(Index+1)
            Returns.append(Code[Parameters[0]])
            Index=Index+2
        elif int(str(Code[Index])[-2:])==5:
            if len(str(Code[Index]))<4:
                Parameters.append(Code[Index+2])
            elif int(str(Code[Index])[len(str(Code[Index]))-4])==0:
                Parameters.append(Code[Index+2])
            elif int(str(Code[Index])[len(str(Code[Index]))-4])==2:
                Parameters.append(Code[Index+2]+RelativeBase)
            else:
                Parameters.append(Index+2)
            if len(str(Code[Index]))<3:
                Parameters.append(Code[Index+1])
            elif int(str(Code[Index])[len(str(Code[Index]))-3])==0:
                Parameters.append(Code[Index+1])
            elif int(str(Code[Index])[len(str(Code[Index]))-3])==2:
                Parameters.append(Code[Index+1]+RelativeBase)
            else:
                Parameters.append(Index+1)
            if Code[Parameters[1]]==0:
                Index+=3
            else:
                Index=Code[Parameters[0]]
        elif int(str(Code[Index])[-2:])==6:
            if len(str(Code[Index]))<4:
                Parameters.append(Code[Index+2])
            elif int(str(Code[Index])[len(str(Code[Index]))-4])==0:
                Parameters.append(Code[Index+2])
            elif int(str(Code[Index])[len(str(Code[Index]))-4])==2:
                Parameters.append(Code[Index+2]+RelativeBase)
            else:
                Parameters.append(Index+2)
            if len(str(Code[Index]))<3:
                Parameters.append(Code[Index+1])
            elif int(str(Code[Index])[len(str(Code[Index]))-3])==0:
                Parameters.append(Code[Index+1])
            elif int(str(Code[Index])[len(str(Code[Index]))-3])==2:
                Parameters.append(Code[Index+1]+RelativeBase)
            else:
                Parameters.append(Index+1)
            if Code[Parameters[1]]==0:
                Index=Code[Parameters[0]]
            else:
                Index+=3
        elif int(str(Code[Index])[-2:])==7:
            if len(str(Code[Index]))<5:
                Parameters.append(Code[Index+3])
            elif int(str(Code[Index])[len(str(Code[Index]))-5])==0:
                Parameters.append(Code[Index+3])
            elif int(str(Code[Index])[len(str(Code[Index]))-5])==2:
                Parameters.append(Code[Index+3]+RelativeBase)
            else:
                Parameters.append(Index+3)
            if len(str(Code[Index]))<4:
                Parameters.append(Code[Index+2])
            elif int(str(Code[Index])[len(str(Code[Index]))-4])==0:
                Parameters.append(Code[Index+2])
            elif int(str(Code[Index])[len(str(Code[Index]))-4])==2:
                Parameters.append(Code[Index+2]+RelativeBase)
            else:
                Parameters.append(Index+2)
            if len(str(Code[Index]))<3:
                Parameters.append(Code[Index+1])
            elif int(str(Code[Index])[len(str(Code[Index]))-3])==0:
                Parameters.append(Code[Index+1])
            elif int(str(Code[Index])[len(str(Code[Index]))-3])==2:
                Parameters.append(Code[Index+1]+RelativeBase)
            else:
                Parameters.append(Index+1)
            if Code[Parameters[2]]<Code[Parameters[1]]:
                Code[Parameters[0]]=1
            else:
                Code[Parameters[0]]=0
            Index+=4
        elif int(str(Code[Index])[-2:])==8:
            if len(str(Code[Index]))<5:
                Parameters.append(Code[Index+3])
            elif int(str(Code[Index])[len(str(Code[Index]))-5])==0:
                Parameters.append(Code[Index+3])
            elif int(str(Code[Index])[len(str(Code[Index]))-5])==2:
                Parameters.append(Code[Index+3]+RelativeBase)
            else:
                Parameters.append(Index+3)
            if len(str(Code[Index]))<4:
                Parameters.append(Code[Index+2])
            elif int(str(Code[Index])[len(str(Code[Index]))-4])==0:
                Parameters.append(Code[Index+2])
            elif int(str(Code[Index])[len(str(Code[Index]))-4])==2:
                Parameters.append(Code[Index+2]+RelativeBase)
            else:
                Parameters.append(Index+2)
            if len(str(Code[Index]))<3:
                Parameters.append(Code[Index+1])
            elif int(str(Code[Index])[len(str(Code[Index]))-3])==0:
                Parameters.append(Code[Index+1])
            elif int(str(Code[Index])[len(str(Code[Index]))-3])==2:
                Parameters.append(Code[Index+1]+RelativeBase)
            else:
                Parameters.append(Index+1)
            if Code[Parameters[2]]==Code[Parameters[1]]:
                Code[Parameters[0]]=1
            else:
                Code[Parameters[0]]=0
            Index+=4
        elif int(str(Code[Index])[-2:])==9:
            if len(str(Code[Index]))<3:
                Parameters.append(Code[Index+1])
            elif int(str(Code[Index])[len(str(Code[Index]))-3])==0:
                Parameters.append(Code[Index+1])
            elif int(str(Code[Index])[len(str(Code[Index]))-3])==2:
                Parameters.append(Code[Index+1]+RelativeBase)
            else:
                Parameters.append(Index+1)
            RelativeBase+=Code[Parameters[0]]
            Index=Index+2
        else:
            print("ERROR")
            print(Index)
            print(Code[Index])
            break
        if len(Returns)==2:
            break
    else:
        return("End",Code,Index,RelativeBase)
    return(Returns,Code,Index,RelativeBase)
    

Code=[]
Memory=100000
Index=0
RelativeBase=0
for _ in range(Memory):
    Code.append(0)
while True:
    Inputs=[input()]
    Returns,Code,Index,RelativeBase=RunIntcode(Code,Inputs,Index,RelativeBase)

