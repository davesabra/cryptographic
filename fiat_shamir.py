
# fiat-shamir (heuristic) is to replace the interaction with the single verifier 'Victor' with non-interactive random oracle:
from random import seed
from random import randint
seed(1)

def assert_equals(a,b):
    return a == b
        
# non-interactive zn proof

# Peggy wants to prove she knows the discrete log x where y = g^x but without revealing it to ANYONE
# she picks a random k and computes t = g^k 
g = 2
x = 3                # x has to be initialised for the demo but in principle it is secret to Peggy   
y = 8     
k = randint(1, 9)

t = pow(g, k)          

# she computes her own hash function c = H(g,y,t)
publics = (g, y, t)                   # note this has to be a Python tuple  (immut)
c = hash(publics)

# she computes
s = k + c                          

# Peggys statement of proof is the pair (t, s)

print( assert_equals(pow(g,s), t*pow(y,c) ) )

# the algorithm doesnt reveal x but proves Peggy must know its value





















