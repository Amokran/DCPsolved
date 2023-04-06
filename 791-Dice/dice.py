import os, sys
def throw_dice(N,faces,total):
    
    if N==0:
        return
    
    j=1
    lsuma = []
    while (j <= faces):
        if (j+(N-i) >= total):
            i=i
        ++j

    return suma()

def suma_lista(lsuma):
    sumatorio=0
    for el in lsuma:
        sumatorio += el
    return sumatorio    

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
    #throw_dice(N,faces,total)
    
main()

