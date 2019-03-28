import random

Matrix = lambda r,c,k: [[ random.randrange(1,k) for x in range(c)] for y in range(r)] 


def main():

    c=int(input('choose columns= '))
    r=int(input('choose rows=  '))
    k=int(input('range of k= '))

    print(Matrix(r, c, k))
main()
