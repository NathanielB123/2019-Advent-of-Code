#Part 1/2
Code=[3,225,1,225,6,6,1100,1,238,225,104,0,1102,89,49,225,1102,35,88,224,101,-3080,224,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,1101,25,33,224,1001,224,-58,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1102,78,23,225,1,165,169,224,101,-80,224,224,4,224,102,8,223,223,101,7,224,224,1,224,223,223,101,55,173,224,1001,224,-65,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,2,161,14,224,101,-3528,224,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1002,61,54,224,1001,224,-4212,224,4,224,102,8,223,223,1001,224,1,224,1,223,224,223,1101,14,71,225,1101,85,17,225,1102,72,50,225,1102,9,69,225,1102,71,53,225,1101,10,27,225,1001,158,34,224,101,-51,224,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,102,9,154,224,101,-639,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,226,226,224,102,2,223,223,1006,224,329,101,1,223,223,1007,677,677,224,1002,223,2,223,1005,224,344,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,359,1001,223,1,223,108,226,677,224,1002,223,2,223,1005,224,374,1001,223,1,223,107,226,677,224,102,2,223,223,1006,224,389,101,1,223,223,1107,226,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,419,101,1,223,223,1007,226,226,224,102,2,223,223,1006,224,434,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,449,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,464,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,479,101,1,223,223,1008,226,677,224,1002,223,2,223,1006,224,494,101,1,223,223,1107,226,677,224,1002,223,2,223,1005,224,509,1001,223,1,223,1108,226,226,224,1002,223,2,223,1006,224,524,101,1,223,223,7,226,226,224,102,2,223,223,1006,224,539,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,554,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,569,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,584,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,599,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,614,101,1,223,223,108,677,677,224,102,2,223,223,1005,224,629,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,644,1001,223,1,223,7,677,226,224,102,2,223,223,1006,224,659,1001,223,1,223,1007,226,677,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226]
Index=0
while not Code[Index]==99:
    Parameters=[]
    if int(str(Code[Index])[-2:])==1:
        Parameters.append(Code[Index+3])
        if len(str(Code[Index]))<4:
            Parameters.append(Code[Index+2])
        elif int(str(Code[Index])[len(str(Code[Index]))-4])==0:
            Parameters.append(Code[Index+2])
        else:
            Parameters.append(Index+2)
        if len(str(Code[Index]))<3:
            Parameters.append(Code[Index+1])
        elif int(str(Code[Index])[len(str(Code[Index]))-3])==0:
            Parameters.append(Code[Index+1])
        else:
            Parameters.append(Index+1)
        Code[Parameters[0]]=Code[Parameters[1]]+Code[Parameters[2]]
        Index=Index+4
    elif int(str(Code[Index])[-2:])==2:
        Parameters.append(Code[Index+3])
        if len(str(Code[Index]))<4:
            Parameters.append(Code[Index+2])
        elif int(str(Code[Index])[len(str(Code[Index]))-4])==0:
            Parameters.append(Code[Index+2])
        else:
            Parameters.append(Index+2)
        if len(str(Code[Index]))<3:
            Parameters.append(Code[Index+1])
        elif int(str(Code[Index])[len(str(Code[Index]))-3])==0:
            Parameters.append(Code[Index+1])
        else:
            Parameters.append(Index+1)
        Code[Parameters[0]]=Code[Parameters[1]]*Code[Parameters[2]]
        Index=Index+4
    elif int(str(Code[Index])[-2:])==3:
        Code[Code[Index+1]]=int(input())
        Index=Index+2
    elif int(str(Code[Index])[-2:])==4:
        if len(str(Code[Index]))<3:
            Parameters.append(Code[Index+1])
        elif int(str(Code[Index])[len(str(Code[Index]))-3])==0:
            Parameters.append(Code[Index+1])
        else:
            Parameters.append(Index+1)
        print(Code[Parameters[0]])
        Index=Index+2
    elif int(str(Code[Index])[-2:])==5:
        if len(str(Code[Index]))<4:
            Parameters.append(Code[Index+2])
        elif int(str(Code[Index])[len(str(Code[Index]))-4])==0:
            Parameters.append(Code[Index+2])
        else:
            Parameters.append(Index+2)
        if len(str(Code[Index]))<3:
            Parameters.append(Code[Index+1])
        elif int(str(Code[Index])[len(str(Code[Index]))-3])==0:
            Parameters.append(Code[Index+1])
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
        else:
            Parameters.append(Index+2)
        if len(str(Code[Index]))<3:
            Parameters.append(Code[Index+1])
        elif int(str(Code[Index])[len(str(Code[Index]))-3])==0:
            Parameters.append(Code[Index+1])
        else:
            Parameters.append(Index+1)
        if Code[Parameters[1]]==0:
            Index=Code[Parameters[0]]
        else:
            Index+=3
    elif int(str(Code[Index])[-2:])==7:
        Parameters.append(Code[Index+3])
        if len(str(Code[Index]))<4:
            Parameters.append(Code[Index+2])
        elif int(str(Code[Index])[len(str(Code[Index]))-4])==0:
            Parameters.append(Code[Index+2])
        else:
            Parameters.append(Index+2)
        if len(str(Code[Index]))<3:
            Parameters.append(Code[Index+1])
        elif int(str(Code[Index])[len(str(Code[Index]))-3])==0:
            Parameters.append(Code[Index+1])
        else:
            Parameters.append(Index+1)
        if Code[Parameters[2]]<Code[Parameters[1]]:
            Code[Parameters[0]]=1
        else:
            Code[Parameters[0]]=0
        Index+=4
    elif int(str(Code[Index])[-2:])==8:
        Parameters.append(Code[Index+3])
        if len(str(Code[Index]))<4:
            Parameters.append(Code[Index+2])
        elif int(str(Code[Index])[len(str(Code[Index]))-4])==0:
            Parameters.append(Code[Index+2])
        else:
            Parameters.append(Index+2)
        if len(str(Code[Index]))<3:
            Parameters.append(Code[Index+1])
        elif int(str(Code[Index])[len(str(Code[Index]))-3])==0:
            Parameters.append(Code[Index+1])
        else:
            Parameters.append(Index+1)
        if Code[Parameters[2]]==Code[Parameters[1]]:
            Code[Parameters[0]]=1
        else:
            Code[Parameters[0]]=0
        Index+=4
    else:
        print("ERROR")
        print(Index)
        print(Code[Index])
        break


