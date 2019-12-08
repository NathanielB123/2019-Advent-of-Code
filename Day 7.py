#Part 1/2
class Amplifier():
    def __init__(self, Phase, Signal):
        self.Phase=Phase
        self.Signal=Signal

    def Compute(self):
        Code=[3,8,1001,8,10,8,105,1,0,0,21,46,55,76,89,106,187,268,349,430,99999,3,9,101,4,9,9,1002,9,2,9,101,5,9,9,1002,9,2,9,101,2,9,9,4,9,99,3,9,1002,9,5,9,4,9,99,3,9,1001,9,2,9,1002,9,4,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,4,9,1001,9,4,9,102,5,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,99]
        Index=0
        InputNum=0
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
                if InputNum==0:
                    Code[Code[Index+1]]=self.Phase
                    InputNum=1
                else:
                    Code[Code[Index+1]]=self.Signal
                Index=Index+2
            elif int(str(Code[Index])[-2:])==4:
                if len(str(Code[Index]))<3:
                    Parameters.append(Code[Index+1])
                elif int(str(Code[Index])[len(str(Code[Index]))-3])==0:
                    Parameters.append(Code[Index+1])
                else:
                    Parameters.append(Index+1)
                return(Code[Parameters[0]])
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
Amplifiers=[]
Options=[0,1,2,3,4]
Highest=[0,0]
S1=0
for P1 in range(0,5):
    for P2 in range(0,5):
        for P3 in range(0,5):
            for P4 in range(0,5):
                for P5 in range(0,5):
                    if not (P1 in [P2,P3,P4,P5] or P2 in [P1,P3,P4,P5] or P3 in [P2,P1,P4,P5] or P4 in [P2,P3,P1,P5] or P5 in [P2,P3,P4,P1]):
                        Amplifiers.append(Amplifier(P1,S1))
                        SCarry = Amplifiers[len(Amplifiers)-1].Compute()
                        Amplifiers.append(Amplifier(P2,SCarry))
                        SCarry = Amplifiers[len(Amplifiers)-1].Compute()
                        Amplifiers.append(Amplifier(P3,SCarry))
                        SCarry = Amplifiers[len(Amplifiers)-1].Compute()
                        Amplifiers.append(Amplifier(P4,SCarry))
                        SCarry = Amplifiers[len(Amplifiers)-1].Compute()
                        Amplifiers.append(Amplifier(P5,SCarry))
                        SCarry = Amplifiers[len(Amplifiers)-1].Compute()
                        if SCarry>Highest[0]:
                            Highest[0]=SCarry
                            Highest[1]=[P1,P2,P3,P4,P5]
print(Highest[0])


