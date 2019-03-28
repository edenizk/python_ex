f = open('my_file.txt', 'w')
f.write("Hello there!")
f.close()


f = open('my_file.txt', 'r')
file_data = f.read()
print(file_data)
f.close()
 
