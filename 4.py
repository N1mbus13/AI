
import random

def f(x):
    return -(x*x-4*x+6)

x=random.uniform(-5,5)

for i in range(100):
    n=x+random.uniform(-0.1,0.1)
    if f(n)>f(x):
        x=n

print("Best x =",round(x,3))
print("Value =",round(f(x),3))
