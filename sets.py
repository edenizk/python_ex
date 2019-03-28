def main():
    numbers = [1, 2, 6, 3, 1, 1, 6] # puts same numbers in same place 1, 2, 3, 6 is output
    unique_nums = set(numbers)
    print(unique_nums)
    
    unique_nums.add(23)
    print(unique_nums)

    fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

    print("watermelon" in fruit)  # check for element

    fruit.add("watermelon")  # add an element
    print(fruit)

    print(fruit.pop())  # remove a random element
    print(fruit)
    print(sorted(fruit))

main()
