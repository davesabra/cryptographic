
# fiat-shamir (heuristic) is to replace Victor with non-interactive random oracle:
from random import seed
from random import randint
seed(1)

def assert_equals(a,b):
    return a == b
        
# non-interactive zn proof
# Let G cyclic Abelian group of order q
q = 11

# Peggy wants to prove she knows the discrete log x where y = g^x but without revealing it to ANYONE
# she picks a random k and computes t = g^k 
g = 2
x = 3     
y = 8     
k = randint(1, 9)

t = pow(g, k)          

# she computes her own c = H(g,y,t)
publics = (g, y, t)                   # note this has to be a Python tuple  (immut)
c = hash(publics)

# she computes
s = k + c                          

# Peggys statement of proof is the pair (t, s)

print( assert_equals(pow(g,s), t*pow(y,c) ) )












# Victor challenges with his own randomness
#c = randint(1,9)
#print(c)

# Peggy computes her response modulo p
#s = k + c*x

# Victor accepts if g^s == t*(y^c)    i.e if x == 
#print(pow(g, s))
#print( t*pow(y, c))

#print(assert_equals(pow(g, s), t*pow(y, c) ))









