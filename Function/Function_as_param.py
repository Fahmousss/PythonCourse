def power(x):
   return lambda n: x**n

def cube_num(x):
   return power(x)(3)

print(cube_num(10))