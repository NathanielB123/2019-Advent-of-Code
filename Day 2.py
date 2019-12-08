#Part 1
Code=[1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,2,19,13,23,1,23,10,27,1,13,27,31,2,31,10,35,1,35,9,39,1,39,13,43,1,13,43,47,1,47,13,51,1,13,51,55,1,5,55,59,2,10,59,63,1,9,63,67,1,6,67,71,2,71,13,75,2,75,13,79,1,79,9,83,2,83,10,87,1,9,87,91,1,6,91,95,1,95,10,99,1,99,13,103,1,13,103,107,2,13,107,111,1,111,9,115,2,115,10,119,1,119,5,123,1,123,2,127,1,127,5,0,99,2,14,0,0]
Index=0
Code[1]=12
Code[2]=2
while not Code[Index]==99:
    if Code[Index]==1:
        Code[Code[Index+3]]=Code[Code[Index+1]]+Code[Code[Index+2]]
        Index=Index+4
    elif Code[Index]==2:
        Code[Code[Index+3]]=Code[Code[Index+1]]*Code[Code[Index+2]]
        Index=Index+4
    else:
        print("ERROR")
        print(Code[Index])
print(Code[0])

#Part 2
import random
NotDone=True
while NotDone:
    Code=[1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,2,19,13,23,1,23,10,27,1,13,27,31,2,31,10,35,1,35,9,39,1,39,13,43,1,13,43,47,1,47,13,51,1,13,51,55,1,5,55,59,2,10,59,63,1,9,63,67,1,6,67,71,2,71,13,75,2,75,13,79,1,79,9,83,2,83,10,87,1,9,87,91,1,6,91,95,1,95,10,99,1,99,13,103,1,13,103,107,2,13,107,111,1,111,9,115,2,115,10,119,1,119,5,123,1,123,2,127,1,127,5,0,99,2,14,0,0]
    Index=0
    Code[1]=random.randint(0,99)
    Code[2]=random.randint(0,99)
    Answer=[Code[1],Code[2]]
    while not Code[Index]==99:
        if Code[Index]==1:
            Code[Code[Index+3]]=Code[Code[Index+1]]+Code[Code[Index+2]]
            Index=Index+4
        elif Code[Index]==2:
            Code[Code[Index+3]]=Code[Code[Index+1]]*Code[Code[Index+2]]
            Index=Index+4
        else:
            print("ERROR")
            print(Code[Index])
    if Code[0]==19690720:
        break
print(100*Answer[0]+Answer[1])

