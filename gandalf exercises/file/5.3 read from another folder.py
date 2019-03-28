path = 'C:\\python exam\\gandalf exercises\\file\\newfile\\data.txt'
with open(path, 'w') as f:
    f.write('heyo')
    
with open(path, 'r') as f:
    f_data = f.read()
    print(f_data)
