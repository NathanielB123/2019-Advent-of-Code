import copy
Positions=[[-3,10,-1],[-12,-10,-5],[-9,0,10],[7,-5,-3]]
Velocities=[]
PreviousStates=[[],[],[]]
Searching=[True,True,True]
print("For part 2 get the LCM of the 3 numbers after the answer to part 1 (this might take a long time)")
for i in range(0,len(Positions)):
    Velocities.append([0,0,0])
    i=-1
while Searching[0] or Searching[1] or Searching[2]:
    i+=1
    PositionsCopy=copy.deepcopy(Positions)
    VelocitiesCopy=copy.deepcopy(Velocities)
    State=[[],[],[]]
    for Dimension in range(0,3):
        if Searching[Dimension]:
            for MoonNum in range(0,len(Positions)):
                State[Dimension].append(copy.deepcopy([Positions[MoonNum][Dimension],Velocities[MoonNum][Dimension]]))
    for Dimension in range(0,3):
        if Searching[Dimension]:
            if len(PreviousStates[Dimension])<2 or not State[Dimension] == PreviousStates[Dimension][1]:
                PreviousStates[Dimension].append(copy.deepcopy(State[Dimension]))
            else:
                print(i)
                Searching[Dimension]=False
    for MoonNum in range(0,len(Positions)):
        for Target in range(0,len(Positions)):
            for Dimension in range(0,3):
                Velocities[MoonNum][Dimension]+=(1-int(PositionsCopy[MoonNum][Dimension]==PositionsCopy[Target][Dimension]))*(
                    int(PositionsCopy[MoonNum][Dimension]>PositionsCopy[Target][Dimension])*-2+1)
        for Dimension in range(0,3):
            Positions[MoonNum][Dimension]+=Velocities[MoonNum][Dimension]
    Energy=0
    for MoonNum in range(0,len(Positions)):
        KinEnergy=0
        PotEnergy=0
        for Dimension in range(0,3):
            KinEnergy+=abs(Velocities[MoonNum][Dimension])
            PotEnergy+=abs(Positions[MoonNum][Dimension])
        Energy+=KinEnergy*PotEnergy
    if i==999:
        print("Part 1: "+str(Energy))

