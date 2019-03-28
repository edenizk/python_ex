import random

def distribution(x):

    counted = {}
    for i,v in enumerate(x):
        if v in counted:
            counted[v] += 1
        else:
            counted[v] = 1

    return counted
def mode(x):
    a = sorted(distribution(x).values())
    return a[-1]

def aritmetic_mean_matrix(my_num):
    result = 0

    for i in range(len(my_num)):
        for j in my_num[i]:
            result += int(j)
    return result

def aritmetic_mean(my_num):
    result = 0

    for x in my_num:
        result += int(x)

    return result/len(my_num)

def random_list(n, k):
    result = []

    for y in range(n):
        rand = random.randrange(1,k)
        result.append(rand)
    return result

def RandomM(my_list):
  

  my_list.sort()

  a=len(my_list)//2
  
  if len(my_list)%2==0:
    middle= (my_list[a] + my_list[a-1])/2
    return middle

  else:
    return my_list[a]

def main():

    L= [3, 4, 6, 2, 1, 2, 4, 5, 1, 4]
    print("Mean= ",aritmetic_mean(L))
    print("Median= ",RandomM(L))
    print("Mode= ", mode(L))
main()
