# Schnorr sigma protocol is a 'knowledge extractor'

# generate random integer values
from random import seed
from random import randint

# seed random number generator
seed(1)
# test generate some integers
#for _ in range(10):
#    value = randint(1, 10)  # from uniform dist
#    print(value)

def assert_equals(a,b):
    return a == b
        
# interactive zn proof
# Peggy wants to prove she knows the discrete log x (pvte to Peggy) of y w.r.t g   (y = g^x)
# for  base g  in some finite Abelian group G of prime order p.
# she picks a random k {   k should be from the Z/pZ bucket but any k works because k and c drop out}
# and computes t = g^k and sends it to Victor
g = 2
x = 3    # private to Peggy but has to be initialised in Py 
y = 8    # public 
k = randint(1, 9)  # private to Peggy

t = pow(g, k)           # commitment
#print(t)

# Victor challenges with his own randomness
c = randint(1,9)
#print(c)

# Peggy computes her response (modulo p if you draw from Z/pZ)
s = k + c*x

# Victor accepts if g^s == t*(y^c)    
print(pow(g, s))
print( t*pow(y, c))

print(assert_equals(pow(g, s), t*pow(y, c) ))














