import time
Input="59708372326282850478374632294363143285591907230244898069506559289353324363446827480040836943068215774680673708005813752468017892971245448103168634442773462686566173338029941559688604621181240586891859988614902179556407022792661948523370366667688937217081165148397649462617248164167011250975576380324668693910824497627133242485090976104918375531998433324622853428842410855024093891994449937031688743195134239353469076295752542683739823044981442437538627404276327027998857400463920633633578266795454389967583600019852126383407785643022367809199144154166725123539386550399024919155708875622641704428963905767166129198009532884347151391845112189952083025"
Pattern=[0,1,0,-1]
Debug=time.time()
for z in range(0,100):
    Output=""
    Index=0
    while len(Output)<len(str(Input)):
        Index+=1
        NewPattern=[]
        for i in Pattern:
            for _ in range(0,Index):
                NewPattern.append(i)
        TempIndex=0
        Num=0
        for i in Input:
            TempIndex+=1
            if TempIndex>len(NewPattern)-1:
                TempIndex=0
            Num+=int(i)*NewPattern[TempIndex]
        Output=Output+str(int(abs(Num)%10))
    Input=Output
    if Debug+5<time.time():
        Debug=time.time()
        print(z)
print("Part 1: "+Output[0:8])

#Part 2 doesn't work - still a WIP
RepeatInput="03036732577212944063491565474664"
Offset=int(RepeatInput[0:7])
Length=10000*len(RepeatInput)
for z in range(0,100):
    OutputIndex=Offset-1
    Output=""
    Debug=time.time()
    while OutputIndex<Length:
        OutputIndex+=1
        RepeatInputIndex=OutputIndex%len(RepeatInput)
        InputIndex=OutputIndex
        Num=0
        while InputIndex<Length:
            RepeatInputIndex+=1
            InputIndex+=1
            if RepeatInputIndex>len(RepeatInput)-1:
                RepeatInputIndex=0
            if InputIndex>OutputIndex:
                Num+=int(RepeatInput[RepeatInputIndex])
            else:
                print("ERROR")
        Output=Output+str(int(abs(Num)%10))
        if len(Output)==10:
            Repeat=Output
        elif len(Output)>10:
            if Output[len(Output)-10:]==Repeat:
                RepeatInput=Output[:len(Output)-10]
                break
    else:
        RepeatInput=Output
    print(z+1)
    print(time.time()-Debug)
print(Output[:8])
