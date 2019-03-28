import random
random_num = lambda : random.uniform(1,10)

def RandomM(result):
  
  result.sort()
  print(result)

  a=len(result)//2
  
  if len(result)%2==0:
    middle= (result[a] + result[a-1])/2
    return middle

  else:
    return result[a]

def geomean(my_num):
    result = 1

    for x in my_num:
        result *= int(x)

    return result**(1/len(my_num))

def main():
    L = []
    for i in range(99):

        L.append(random_num())
    print("median = ",RandomM(L))
    print("Geometric Mean = ", geomean(L))
main()
