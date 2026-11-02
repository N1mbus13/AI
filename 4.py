import random

def f(x):
    return -(x**2 - 4*x + 6)

def hill_climb(iterations=100, step=0.1):
    x = random.uniform(-5, 5)

    for i in range(iterations):
        new_x = x + random.uniform(-step, step)

        if f(new_x) > f(x):
            x = new_x

    return x, f(x)

x, value = hill_climb()

print("Best x =", round(x, 3))
print("Value =", round(value, 3))

