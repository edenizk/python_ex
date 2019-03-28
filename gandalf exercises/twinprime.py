import sys

def TwinPrime(n):
     
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
      # Print all prime numbers
    prime_num = []
    for p in range(2, n):
        if prime[p]:
            prime_num.append(p)
    if len(prime_num) % 2 == 1:
        n = len(prime_num) - 1
    else:
        n = len(prime_num)
    counter = 1
    num_pair = 1
    a = str(num_pair) + "- "
    for p in range(0, n, 2):
        print("{}- {}-{}".format(counter, prime_num[p], prime_num[p+1]))
        counter +=1

       


def main():

    TwinPrime(100)


main()
