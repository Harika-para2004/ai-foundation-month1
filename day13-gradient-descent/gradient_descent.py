"""
Day 13 — Gradient Descent from Scratch

Goal:
Minimize the function f(x) = x^2 using gradient descent
"""

# Function we want to minimize
def f(x):
    return x ** 2


# Derivative of the function (slope)
def df(x):
    return 2 * x


# Gradient Descent Implementation
def gradient_descent(start_x, learning_rate, iterations):
    x = start_x

    print("Iteration | x value | f(x)")
    print("-" * 30)

    for i in range(iterations):
        gradient = df(x)
        x = x - learning_rate * gradient

        print(f"{i:9} | {x:7.5f} | {f(x):7.5f}")

    return x


# Run gradient descent
final_x = gradient_descent(
    start_x=10.0,       # starting far from minimum
    learning_rate=0.1,  # step size
    iterations=20
)

print("\nFinal x:", final_x)
print("Minimum value f(x):", f(final_x))
