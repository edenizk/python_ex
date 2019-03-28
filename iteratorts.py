def my_range(x):
    i = 0
    while i < x:
        yield i
        i +=1

def main():

    for n in my_range(4):
        print(n)

    
main()
