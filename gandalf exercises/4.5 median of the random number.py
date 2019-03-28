import random
def RandomM(n, k):
  
  result=[]
  
  while n>0:
      rand = random.randrange(1,k)
      result.append(rand)
      n-=1

  result.sort()
  print(result)

  a=len(result)//2
  
  if len(result)%2==0:
    middle= (result[a] + result[a-1])/2
    return middle

  else:
    return result[a]

def main():
    n = int(input('how many numbers in list='))
    k = int(input('range='))
    print(RandomM(n, k))

main()
