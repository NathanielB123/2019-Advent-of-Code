import math
Input="""#.#.##..#.###...##.#....##....###
...#..#.#.##.....#..##.#...###..#
####...#..#.##...#.##..####..#.#.
..#.#..#...#..####.##....#..####.
....##...#.##...#.#.#...#.#..##..
.#....#.##.#.##......#..#..#..#..
.#.......#.....#.....#...###.....
#.#.#.##..#.#...###.#.###....#..#
#.#..........##..###.......#...##
#.#.........##...##.#.##..####..#
###.#..#####...#..#.#...#..#.#...
.##.#.##.........####.#.#...##...
..##...#..###.....#.#...#.#..#.##
.#...#.....#....##...##...###...#
###...#..#....#............#.....
.#####.#......#.......#.#.##..#.#
#.#......#.#.#.#.......##..##..##
.#.##...##..#..##...##...##.....#
#.#...#.#.#.#.#..#...#...##...#.#
##.#..#....#..##.#.#....#.##...##
...###.#.#.......#.#..#..#...#.##
.....##......#.....#..###.....##.
........##..#.#........##.......#
#.##.##...##..###.#....#....###.#
..##.##....##.#..#.##..#.....#...
.#.#....##..###.#...##.#.#.#..#..
..#..##.##.#.##....#...#.........
#...#.#.#....#.......#.#...#..#.#
...###.##.#...#..#...##...##....#
...#..#.#.#..#####...#.#...####.#
##.#...#..##..#..###.#..........#
..........#..##..#..###...#..#...
.#.##...#....##.....#.#...##...##"""
Input=Input.split("\n")
Largest=0
Temp=[0,0]
Accuracy=3
for y in range(0,len(Input)):
    for x in range(0,len(Input[0])):
        if Input[y][x]=="#":
            Gradients=[]
            for y2 in range(0,len(Input)):
                for x2 in range(0,len(Input[y])):
                    if not (x==x2 and y==y2) and Input[y2][x2]=="#":
                        if not [round((x2-x)/math.sqrt((x2-x)**2+(y2-y)**2),Accuracy),round((y2-y)/math.sqrt((x2-x)**2+(y2-y)**2),Accuracy)] in Gradients:
                            Gradients.append([round((x2-x)/math.sqrt((x2-x)**2+(y2-y)**2),Accuracy),round((y2-y)/math.sqrt((x2-x)**2+(y2-y)**2),Accuracy)])
            if len(Gradients)>Largest:
                Largest=len(Gradients)
                Temp=[x,y]
print(Largest)
#Part 2
Vaporised=0
x=Temp[0]
y=Temp[1]
#Add position of sensor for debug:
Temp=Input[y]
Temp2=""
for x3 in range(0,len(Temp)):
    if not x3 == x:
        Temp2=Temp2+Temp[x3]
    else:
        Temp2=Temp2+"B"
Input[y]=Temp2
#
Gradients=[]
while Vaporised<200:
    Direction=[1,1]
    MaxGoodness=-10
    ToDestroy=["ERROR","ERROR"]
    for y2 in range(0,len(Input)):
        for x2 in range(0,len(Input[0])):
            if not (x==x2 and y==y2) and Input[y2][x2]=="#":
                yR=len(Input)-y-1 #Reverses y co-ordinate so it goes from the more natural to think about, up is higher
                y2R=len(Input)-y2-1
                if not [round((x2-x)/math.sqrt((x2-x)**2+(y2R-yR)**2),Accuracy),round((y2R-yR)/math.sqrt((x2-x)**2+(y2R-yR)**2),Accuracy)] in Gradients:
                    UnitVector=[round((x2-x)/math.sqrt((x2-x)**2+(y2R-yR)**2),Accuracy),round((y2R-yR)/math.sqrt((x2-x)**2+(y2R-yR)**2),Accuracy)]
                    if UnitVector[0]>=0 and UnitVector[1]>=0:
                        Goodness=1+UnitVector[1]-math.sqrt((x2-x)**2+(y2R-yR)**2)*0.0001
                    elif UnitVector[0]>=0 and UnitVector[1]<=0:
                        Goodness=UnitVector[0]-math.sqrt((x2-x)**2+(y2R-yR)**2)*0.0001
                    elif UnitVector[0]<=0 and UnitVector[1]<=0:
                        Goodness=UnitVector[0]-math.sqrt((x2-x)**2+(y2R-yR)**2)*0.0001
                    elif UnitVector[0]<=0 and UnitVector[1]>=0:
                        Goodness=-1-UnitVector[1]-math.sqrt((x2-x)**2+(y2R-yR)**2)*0.0001
                    if Goodness>MaxGoodness:
                        MaxGoodness=Goodness
                        ToDestroy=[x2,y2]
                        Debug=UnitVector.copy()
    if not ToDestroy[0]=="ERROR":
        Vaporised+=1
        Temp=Input[ToDestroy[1]]
        Temp2=""
        for x3 in range(0,len(Temp)):
            if not x3 == ToDestroy[0]:
                Temp2=Temp2+Temp[x3]
            else:
                Temp2=Temp2+"X"
        Input[ToDestroy[1]]=Temp2
        x2=ToDestroy[0]
        yR=len(Input)-y-1
        y2R=len(Input)-ToDestroy[1]-1
        Gradients.append([round((x2-x)/math.sqrt((x2-x)**2+(y2R-yR)**2),Accuracy),round((y2R-yR)/math.sqrt((x2-x)**2+(y2R-yR)**2),Accuracy)])
    else:
        Gradients=[]
print(ToDestroy[0]*100+ToDestroy[1])
                                

