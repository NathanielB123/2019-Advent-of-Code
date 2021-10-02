from functools import cache

Input ="""
             Z L X W       C                 
             Z P Q B       K                 
  ###########.#.#.#.#######.###############  
  #...#.......#.#.......#.#.......#.#.#...#  
  ###.#.#.#.#.#.#.#.###.#.#.#######.#.#.###  
  #.#...#.#.#...#.#.#...#...#...#.#.......#  
  #.###.#######.###.###.#.###.###.#.#######  
  #...#.......#.#...#...#.............#...#  
  #.#########.#######.#.#######.#######.###  
  #...#.#    F       R I       Z    #.#.#.#  
  #.###.#    D       E C       H    #.#.#.#  
  #.#...#                           #...#.#  
  #.###.#                           #.###.#  
  #.#....OA                       WB..#.#..ZH
  #.###.#                           #.#.#.#  
CJ......#                           #.....#  
  #######                           #######  
  #.#....CK                         #......IC
  #.###.#                           #.###.#  
  #.....#                           #...#.#  
  ###.###                           #.#.#.#  
XF....#.#                         RF..#.#.#  
  #####.#                           #######  
  #......CJ                       NM..#...#  
  ###.#.#                           #.###.#  
RE....#.#                           #......RF
  ###.###        X   X       L      #.#.#.#  
  #.....#        F   Q       P      #.#.#.#  
  ###.###########.###.#######.#########.###  
  #.....#...#.....#.......#...#.....#.#...#  
  #####.#.###.#######.#######.###.###.#.#.#  
  #.......#.......#.#.#.#.#...#...#...#.#.#  
  #####.###.#####.#.#.#.#.###.###.#.###.###  
  #.......#.....#.#...#...............#...#  
  #############.#.#.###.###################  
               A O F   N                     
               A A D   M                     """.split("\n")

Input.pop(0)
Input = tuple(Input)

@cache
def GetPortalIDAndStartPos(Maze, Pos):
    Moves = ((0, -1), (-1, 0), (1, 0), (0, 1))
    ID = Maze[Pos[0]][Pos[1]]
    PossiblePosA = None
    PossiblePosB = None
    for i in range(len(Moves)):
        Move = Moves[i]
        NewPos = (Pos[0] + Move[0], Pos[1] + Move[1])
        if NewPos[0] >= 0 and NewPos[0] < len(Maze) and NewPos[1] >= 0 and NewPos[1] < len(Maze[NewPos[0]]):
            if Maze[NewPos[0]][NewPos[1]] == ".":
                PossiblePosA = NewPos
            elif not Maze[NewPos[0]][NewPos[1]] in ("#", " "):
                # If going up or left, need to reverse ID and always read down or freom left to right
                if i <= 1:
                    ID = Maze[NewPos[0]][NewPos[1]] + ID
                else:
                    ID = ID + Maze[NewPos[0]][NewPos[1]]
                # Position of start might also be 1 further along in direction of portal
                PossiblePosB = (NewPos[0] + Move[0], NewPos[1] + Move[1])
    #print(ID, Pos)
    Pos = PossiblePosB if PossiblePosA is None else PossiblePosA
    return ID, Pos

@cache
def FloodFill(Maze, PrevDone, Pos):
    #print(Keys)
    ToFill = [[-1 for y in range(len(Maze[x]))] for x in range(len(Maze))]
    Goals = dict()
    ToFill[Pos[0]][Pos[1]] = 0
    Moves = ((0, 1), (1, 0), (-1, 0), (0, -1))
    Done = False
    PotPos = [Pos]
    Steps = 0
    while not Done:
        Done = True
        Steps+=1
        NewPos = []
        for Pos in PotPos:
            for Move in Moves:
                TPos = (Pos[0] + Move[0], Pos[1] + Move[1])
                if TPos[0] >= 0 and TPos[0] < len(Maze) and TPos[1] >= 0 and TPos[1] < len(Maze[TPos[0]]):
                    if ToFill[TPos[0]][TPos[1]] == -1:
                        Tile = Maze[TPos[0]][TPos[1]]
                        if Tile == ".":
                            ToFill[TPos[0]][TPos[1]] = Steps
                            NewPos.append(TPos)
                            Done = False
                        elif Tile == "#" or Tile == " ":
                            ToFill[TPos[0]][TPos[1]] = -2
                        else:
                            ToFill[TPos[0]][TPos[1]] = -3
                            ID, _ = GetPortalIDAndStartPos(Maze, TPos)
                            if ID not in Goals and ID not in PrevDone:
                                Goals[ID] = (TPos, Steps)
        PotPos = NewPos
    #print(ToFill)
    return Goals

@cache
def Dist(PosA, PosB):
    return abs(PosA[0] - PosB[0]) + abs(PosA[1] - PosB[1])

@cache
def Teleport(Maze, ID, Pos):
    Moves = ((0, 1), (1, 0), (-1, 0), (0, -1))
    for x in range(len(Maze)):
        for y in range(len(Maze[x])):
            if Maze[x][y] not in ("#", ".", " ") and Maze[x][y] in ID:
                PortalID, PortalPos = GetPortalIDAndStartPos(Maze, (x,y))
                if PortalID == ID and Dist(PortalPos, Pos) > 1:
                    return PortalPos

def GetIfOuter(Maze, Pos):
    if Pos[0] <= 1 or Pos[0] >= len(Maze) - 2 or Pos[1] <= 1 or Pos[1] >= len(Maze[Pos[0]]) - 2:
        return True
    else:
        return False
                    
                    

@cache
def RecursiveTry(Maze, Pos, PrevDone, Steps):
    Options = FloodFill(Maze, PrevDone, Pos)
    NewSteps = None
    if len(Options.keys()) > 0:
        for Opt in Options.keys():
            #print("".join([" " for _ in range(Steps)]) + Opt + ": ")
            if Opt == "ZZ":
                Temp = Steps + Options[Opt][1] - 1
            else:
                Temp = RecursiveTry(Maze, Teleport(Maze,Opt,Options[Opt][0]), frozenset(list(PrevDone)+[Opt]), Steps + Options[Opt][1])
            if Temp is not None:
                if NewSteps is None:
                    NewSteps = Temp
                else:
                    NewSteps = min(Temp, NewSteps)
            #print("".join([" " for _ in range(Steps)]) + Opt + " "+str(Temp))
        return NewSteps
    else:
        return None

def Main(Maze):
    print(RecursiveTry(Maze, Teleport(Maze, "AA", (-10, -10)), frozenset(["AA"]),0))

Main(Input)
