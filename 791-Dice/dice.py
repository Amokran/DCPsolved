import os, sys
import itertools

DBG = False #Enable (true) to see traces

#this calculates if each of the numbers in the first dice can be part of a solution
#and calls a recursive funtion to obtain the values for the rest of dice to form a solution
def throw_first(N,faces,total):
    solutionpool = []
  
    #Iterate through dice's faces/numbers 
    j=1
    M=N-1 # M = the rest of the dice apart for the one "rolled" here 
    while (j <= faces):
        #check if j can be in some winner combination,
        #for being a candidate, j has to meet two conditions
        if ( ( j + M <= total ) and ( j+ M*faces >= total ) ):
            combination = []
            permutations = []
            
            combination.append(j)
            solution = throw_next(M,faces,total,combination)
            print(f"Solution {j} is: "+str(solution))

            permutations = itertools.permutations(solution)
            for perm in permutations:
               try:
                   pos =  solutionpool.index(perm) #check if the permutation already exists in the solutionpool. If not, then a ValueError is thrown
               except ValueError:                                      
                    solutionpool.append(perm) #permutation didn't exist in the solutionpool, let's add it            
           
        j = j + 1
    return solutionpool

#this is a recursive function
def throw_next(N,faces,total,combination):
    
    if DBG: print(f'*')

    M=N-1 # M = Dice left
    acc = get_acc_value(combination)
    
    #Debug print
    if DBG: print(f"Current Combination: {combination}")
    if DBG: print(f"Accumulated: {acc}")
    if DBG: print(f"Dice left: {M}")
    if DBG: print(f"")
    #Iterate through dice's faces/numbers 
    j=1
    while (j <= faces):
        if DBG: print(f"j is: {j}")
        if DBG: print(f"")
        newcombination=combination
        if M>0:
            if DBG:print(f"{M} dice left..")
            if DBG:print(f"")
            #There is more dice left. Check if this face/number can be in some winner combination
            if ( ( acc + j + M <= total ) and ( acc + j+ M*faces >= total ) ):
                if DBG:print(f"{j} is part of one of the  winning combinations which add up to {total}")
                newcombination.append(j)
                newcombination = throw_next(M,faces,total,newcombination)
                return newcombination
        else:
            if DBG:print(f"This is the last dice")
            #It's the last dice. Check if this face/number adds up to form a winner combination        
            if ( acc + j == total):
                if DBG:print(f"{j} is the last element  of a winning combinations which add up to {total}")
                newcombination.append(j)
                return newcombination
        j = j + 1

def get_acc_value(combination):
    addsupto=0
    for num in combination:
        addsupto = addsupto + num
    return addsupto 

def main():

    N      = int(input("> Set throw number of dice: "))
    faces  = int(input("> Set how many faces: "))
    total  = int(input("> Set total: "))
    summax = N*faces
    summin = N*1
    
    print(f"Max sum will be: {summax}")
    if ( (total > summax) or (total < summin) ):
        print(f"Error: setted total cannot be achieved by trhowing {N} dice of {faces} faces each")
        return
    else:
        print(f"Problem conditions OK")
    
    print(f"Invoking throw_dice({N},{faces},{total})")
    solutions = throw_first(N,faces,total)
    print(f"Below you can see the solutions:")
    print(f"{solutions}") 
    
main()

