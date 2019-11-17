import sys

def assert_equals(a,b):
    return a == b
        
g = 2                                


# Note this is a rubbish algorithm! processes bits one at a time. 'Sliding windows' method is better.

#example5 biggest prime i can do here
e = 131071                   # 1 1111 1111 1111 1111  
l = 17

#example7 biggest int i can compute here
#e = 131072                # 10 0000 0000 0000 0000
#l = 18

#example8 (overflow)
#e = 131073
#l = 18

# e = Σ b(i) 2^i

# digit sets
#e1 =                              (1,1,1,1)                                # works
#e1 =                      (1,1,1,1,1,1,1,1)                          # works
#e1 =              (1,1,1,1,1,1,1,1,1,1,1,1)                   # works
#e1 =      (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)           # works
e1 =    (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)         # works this is the largest prime i can compute in Thonny

#e1 =   (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)       #works this is the largest exponent Thonny will handle, 0x2ffff
#e1 =  (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1)      # overflow!  
#e1 =  (1,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0)        # overflow




def left_to_right_bin_exp(base, bitset):
    A = base
    for i in range(l-1, 0, -1):
        A = A*A
        if bitset[i] == 1  :           # the bits determine which powers get computed
            A = A* pow(g,bitset[i])
            if A > pow(g, e):
                sys.exit()
    return A


res = left_to_right_bin_exp(g, e1)
expect = pow(g,e)

frac_err = (expect-res)//expect

print(frac_err)

print(assert_equals(res, expect))



  


    


