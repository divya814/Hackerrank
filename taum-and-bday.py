# https://www.hackerrank.com/challenges/taum-and-bday/problem

def taumBday(b, w, bc, wc, z):
    # Write your code here
    cost=0
    if b*wc + b*z < b*bc:
        cost= w*wc + b*wc + b*z
    elif w*bc + w*z < w*wc:
        cost= b*bc + w*bc + w*z
    else:
        cost= b*bc + w*wc
    return cost
    
    
### or

def taumBday(b, w, bc, wc, z):
    return b*min(bc,wc+z)+ w*min(wc,bc+z)
   
