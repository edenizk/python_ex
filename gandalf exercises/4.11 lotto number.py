import random
def lotto_num():
    return random.sample(range(80), 10)



def main():

    a = lotto_num()
    print(a)
main()
