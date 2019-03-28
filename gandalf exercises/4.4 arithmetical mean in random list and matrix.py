import random

Matrix = lambda r,c,k: [[ random.randrange(1,k) for x in range(c)] for y in range(r)] 

def aritmetic_mean(my_num):
    result = 0

    for x in my_num:
        result += int(x)

    return result/len(my_num)
def aritmetic_mean_matrix(my_num):
    result = 0

    for i in range(len(my_num)):
        for j in my_num[i]:
            result += int(j)
    return result
def random_list(n, k):
    result = []

    for y in range(n):
        rand = random.randrange(1,k)
        result.append(rand)
    return result

def main():
    c=int(input('choose columns= '))
    r=int(input('choose rows=  '))
    k=int(input('range of k= '))

    n=int(input('how many number in normal list='))
    k=int(input('range of k='))
    randomL = random_list(n,k)
    print(randomL)
    print(aritmetic_mean(randomL),"\n")
    my_matrix = Matrix(r, c, k)
    print(my_matrix)
    print(aritmetic_mean_matrix(my_matrix))
main()
