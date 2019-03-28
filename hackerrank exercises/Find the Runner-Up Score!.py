n = int(input())
arr = list(map(int, input().split()))
arr.sort()
    max_num = arr[-1]
while max_num == arr[-1]:
    arr.remove(arr[-1])
print(arr[-1])
