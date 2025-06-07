def f(x):
    return (x - 1)**2 + 2

def gradient(x):
    return 2 * (x - 1)

x = 3
learning_rate = 0.1
max_iterations = 100
tolerance = 1e-6

for i in range(max_iterations):
    grad = gradient(x)
    x_new = x - learning_rate * grad
    if abs(x_new - x) < tolerance:
        break
    x = x_new

print(f"Minimum at x = {x:.6f}")
print(f"f(x) = {f(x):.6f}")
