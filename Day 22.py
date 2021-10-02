from functools import partial, cache
from time import time

#SIZE = 10007
SIZE = 119315717514047


Instructions = """deal with increment 65
deal into new stack
deal with increment 25
cut -6735
deal with increment 3
cut 8032
deal with increment 71
cut -4990
deal with increment 66
deal into new stack
cut -8040
deal into new stack
deal with increment 18
cut -8746
deal with increment 42
deal into new stack
deal with increment 17
cut -8840
deal with increment 55
cut -4613
deal with increment 10
cut -5301
deal into new stack
deal with increment 21
cut -5653
deal with increment 2
cut 5364
deal with increment 72
cut -3468
deal into new stack
cut -9661
deal with increment 63
cut 6794
deal with increment 43
cut 2935
deal with increment 66
cut -1700
deal with increment 6
cut 5642
deal with increment 64
deal into new stack
cut -5699
deal with increment 43
cut -9366
deal with increment 42
deal into new stack
cut 2364
deal with increment 13
cut 8080
deal with increment 2
deal into new stack
cut -9602
deal with increment 51
cut 3214
deal into new stack
cut -2995
deal with increment 57
cut -8169
deal into new stack
cut 362
deal with increment 41
cut -4547
deal with increment 56
cut -1815
deal into new stack
cut 1554
deal with increment 71
cut 2884
deal with increment 44
cut -2423
deal with increment 4
deal into new stack
deal with increment 20
cut -2242
deal with increment 48
cut -716
deal with increment 29
cut -6751
deal with increment 45
cut -9511
deal with increment 75
cut -440
deal with increment 35
cut 6861
deal with increment 52
cut -4702
deal into new stack
deal with increment 28
cut 305
deal with increment 16
cut 7094
deal into new stack
cut 5175
deal with increment 30
deal into new stack
deal with increment 61
cut 1831
deal into new stack
deal with increment 25
cut 4043"""

def deal_into_new_stack(Deck):
    return Deck[::-1]

def inverse_deal_into_new_stack(Index):
    # Forwards: New index = SIZE - OldIndex - 1
    # Inverse: New index = SIZE - OldIndex - 1
    return SIZE - Index - 1

def cut(Deck, N):
    if N >= 0:
        return Deck[N::]+Deck[0:N]
    else:
        return Deck[N::] + Deck[0:N]

def inverse_cut(Index, N):
    # Forwards: (assuming positive - just to give an idea) New index = branch(index < N){old index + (SIZE - N),old index - N}
    # Inverse: Multiply N by -1 and then (assuming positive - just to give an idea) New index = branch(index < N){old index + (SIZE - N),old index - N}
    N *= -1
    if N >= 0:
        if N > Index:
            return Index + SIZE - N
        else:
            return Index - N
    else:
        if N*-1 > SIZE - Index - 1:
            return Index - N - SIZE
        else:
            return Index - N            
    
    
def deal_with_increment(Deck, N):
    NewDeck = [None for _ in range(SIZE)]
    for i in range(SIZE):
        NewDeck[(N*i)%SIZE] = Deck[i]
    return NewDeck

def inverse_deal_with_increment(Index,N):
    # Forwards: New index = old index * N % size
    # Inverse: New index = old index / N % size (however, division under modulo arithmetic is kinda funky - the actual inverse operation of * here is to take a repeated subtraction of N until you
    # reach 0 and count the number of subtractions - just go with it)

    # Faster than euler's method implemented manually, might get even faster using library such as numpy
    return (pow(N, -1, SIZE) * Index) % SIZE

def inverse_deal_with_increment2(Index, N):
    Iters = 0
    while Index != 0:
        Iters += Index // N
        Index %= N
        if Index == 0:
            break
        else:
            Index = (Index - N)%SIZE
            Iters += 1
    return Iters

def InterpretInstructs(Instructions):
    Instructions = Instructions.split("\n")
    Deck = list(range(SIZE))
    for Instruct in Instructions:
        Instruct = Instruct.split(" ")
        try:
            IsNum = True
            Instruct[-1] = int(Instruct[-1])
        except:
            IsNum = False
        if IsNum:
            Deck = globals()["_".join(Instruct[0:-1])](Deck,Instruct[-1])
        else:
            Deck = globals()["_".join(Instruct)](Deck)
    return Deck

def InterpretInstructsB(Instructions, Index):
    Instructions = Instructions.split("\n")[::-1]
    Prev = 2020
    t = time()
    for i in range(101741582076661):
        for Instruct in Instructions:
            Instruct = ["inverse"]+Instruct.split(" ")
            try:
                IsNum = True
                Instruct[-1] = int(Instruct[-1])
            except:
                IsNum = False
            if IsNum:
                Index = globals()["_".join(Instruct[0:-1])](Index,Instruct[-1])
            else:
                Index = globals()["_".join(Instruct)](Index)
        if Index == 2020:
            raise Exception("REPEAT!!! " + str(Index) + " " + str(i))
        if t+5 < time():
            print(str(100*i/101741582076661) + "% complete, index = "+str(Index))
            t=time()
    return Index

#print(list(map(partial(InterpretInstructsB, Instructions), range(SIZE))))
print(InterpretInstructsB(Instructions,2020))
