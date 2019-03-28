import random

def random_list(n, k):
    result = []
    for y in range(n):
        rand = random.randrange(1,k)
        result.append(rand)
    return result

def main():
    
    n=int(input('how many n='))
    k=int(input('range of k='))
    
    print(random_list(n,k))

main()
