import random
random_num = lambda : random.uniform(1,10)

def main():
    L = []
    for i in range(99):

        L.append(random_num())
    print(sorted(L.split("\n")))
main()
