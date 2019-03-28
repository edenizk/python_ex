#question 1
print_str = "Water falls"

i=0
while i < len(print_str):
    print(print_str[i])
    i +=1

#question2
    
number = 6    
# We'll always start with our product equal to the number
product = number

while number != 1:
    number -=1
    product *= number

print(product)

#question3
number = 6
# We'll start with the product equal to the number
product = number
for num in range(1, number):
    product *= num
print(product)

#question4
start_num = 5#provide some start number
end_num = 100#provide some end number that you stop when you hit
count_by = 2#provide some number to count by 

# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)


#question5
limit = 40

num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)
