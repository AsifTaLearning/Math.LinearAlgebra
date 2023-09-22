from sympy.solvers import linsolve
from sympy import var , Eq

# Solving a linear system
# Gauss's method

var(' x y z ')

eq1 = (1/4)*x + y - z 
eq2 = x + 4*y + 2*z - 12
eq3 = 2*x - 3*y - z -3

ans = linsolve([eq1,eq2,eq3],(x,y,z))

print(ans)

# Another example

var('x y z w')

eq1 = 2*x -3*y -z + 2*w + 2
eq2 = x + 3*z + 1*w - 6
eq3 = 2*x - 3*y -z + 3*w + 3
eq4 = y + z - 2*w -4

ans = linsolve([eq1,eq2,eq3,eq4],(x,y,z,w))

print(ans)

# Another example

var('x y z')

eq1 = x+y+z - 6
eq2 = x +2*y + z - 8
eq3 = 2*x +3*y +2*z -13

ans = linsolve([eq1,eq2,eq3],(x,y,z))

print(ans)

# Another example

var('x y z')

eq1 = -x -y + 3*z -3
eq2 = x + z -3
eq3 = 3*x -y + 7*z -15

ans = linsolve([eq1,eq2,eq3],(x,y,z))

print(ans)

# Another example

var('x y x')

eq1 = x - y + z -4
eq2 = x + y - 2*z +1

ans = linsolve([eq1,eq2],(x,y,z))

print(ans)





