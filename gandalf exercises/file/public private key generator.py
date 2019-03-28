import random
import math
import time

def is_prime(num):
    x = True
    if num > 1:
   # check for factors
        if (num % 2) != 0:
           for i in range(3, int(math.sqrt(num)), 2):
               if (num % i) == 0:
                    x = False
                    break
        else:
            x = False 
    # if input number is less than
    # or equal to 1, it is not prime
    else:
        x = False
    return x

def random_prime_gen():
    a = random.getrandbits(54)
    #print(a)
    x = False
    while x != True:
        x = is_prime(a)
        if x == False:
            a = random.getrandbits(54)

            #print(a,"\n",x)
        #print(x)

    return a

def finding_n(a, b):
    return a*b

def finding_mod(a, b):
    return ((a-1)*(b-1))

def public_e(a, b):
    e = random.getrandbits(54)
    c = math.gcd(e,((a-1)*(b-1)))
    while c != 1:
        e = random.getrandbits(54)
        c = math.gcd(e, finding_mod(a, b))
    return e


def egcd(e, f):
    if e == 0:
        return (f, 0, 1)
    else:
        g, y, x = egcd(f % e, e)
        
        return (g, x - (f // e) * y, y)

def private_d(e, f):
    g, y, x = egcd(e, f)
    
    return y % f
    
def main():
    a = random_prime_gen()
    b = random_prime_gen()
    e = public_e(a, b)
    f = finding_mod(a, b)
    d = private_d(e, f)
    n = finding_n(a, b)
    print("heres your keys: \nq:",a ,"\np:", b,"\ne:", e, "\nd:", d, "\nn:", n, "\n((q-1)*(p-1))= ", f)
    print("public key({}, {}), private key({}, {})".format(n, e, n, d))
    
    print("writing to file.")
    
    with open("private.key", 'w') as f:
        f.write("private key ({}, {})".format(n, d))
        
    time.sleep( 0.3 )
    print("\rwriting to file..")

    with open("public.key", 'w') as f:
        f.write("public key ({}, {})".format(n, e))
        
    time.sleep( 0.3 )
    print("\rwriting to file...")
    time.sleep( 0.3 )
    print("\rwrited")
    input("Press Enter to continue...")


    
main()
