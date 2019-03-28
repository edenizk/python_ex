def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

def main():

    height = int(input('height='))
    radius = int(input('radius='))

    result=cylinder_volume(height,radius)
    print(result)
main()
