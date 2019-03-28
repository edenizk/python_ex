import math
print('TOrus calculator\n')
R=float(input('major radius R = '))
r=float(input('minor radius r = '))
area = (2*math.pi*R)*(2*math.pi*r)
vol = (math.pi*r**2)*(2*math.pi*R)
print("area = ",area)
print("volume = ",vol)
