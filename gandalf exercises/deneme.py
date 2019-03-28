import random
Matrix = lambda r,c,k: [[ random.randrange(1,k) for x in range(c)] for y in range(r)] 


def main():

    asd= Matrix(4,3,10)
    print(asd)
    print(len(asd))
    for i in range(len(asd)):
        for j in asd[i]:
            print(j)
main()
