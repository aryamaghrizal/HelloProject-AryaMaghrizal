import cmath
 
a = int(input('Tulis a: '))
b = int(input('Tulis b: '))
c = int(input('Tulis c: '))
 
d = (b**2) - (4*a*c)
 
x1 = (-b-cmath.sqrt(d))/(2*a)
x2 = (-b+cmath.sqrt(d))/(2*a)
 
print('Hasil Persamaan Kuadrat adalah {0} dan {1}'.format(x1,x2))
