def factorial(n):
    result = 1
    for x in range(1, n + 1):
        result *= x
    return result


def main():


    print(factorial(3))
    
main()
