def equals(a, b):
    a.sort()
    b.sort()
    if a == b:
        return True
    else:
        return False

def main():
    
    print(equals([1,2,3,4],[4,3,2,1,5]))

main()
