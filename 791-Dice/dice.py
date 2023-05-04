import os, sys

def throw_first(N,faces,total):
    combimatrix = []
       
    #Iterate through dice's faces/numbers 
    j=1
    M=N-1
    while (j <= faces):
        #check if this face/number can be in some winner combination
        if ( ( j + M <= total ) and ( j+ M*faces >= total ) ):
              combination = []
              combination.append(j)
              combimatrix[j] = throw_next(M,faces,total,combination)
 
    return combimatrix

def throw_next(N,faces,total,combination):
    
    print('*')

    M=N-1 # M = Dice left
    acc = get_acc_value(combination)
    
    #Debug print
    print(f"Current Combination: {combination}")
    print(f"Accumulated: {acc}")
    print(f"Dice left: {M}")
    
    #Iterate through dice's faces/numbers 
    j=1
    while (j <= faces):
        print(f"j is: {j}")
        if M>0:
            print(f"{M} dice left..")
            #There is more dice left. Check if this face/number can be in some winner combination
            if ( ( acc + j + M <= total ) and ( acc + j+ M*faces >= total ) ):
                print(f"{j} is part of one of the  winning combinations which add up to {total}")
                combination.append(j)
                combination = throw_next(M,faces,total,combination)
        else:
            print(f"This is the last dice")
            #It's the last dice. Check if this face/number adds up to form a winner combination        
            if ( acc + j == total):
                combination.append(j)
                return combination
        j = j + 1

    #return combination

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

