with open('with.txt', 'w') as f:
    f.write('heyo')

with open('with.txt', 'r') as f:
    f_data = f.read()

print(f_data)
