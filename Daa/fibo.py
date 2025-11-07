import time
def fibonacci_iterative(n):
    a, b = 0, 1
    series = []
    steps = 0
    for i in range(n):
        series.append(a)
        a, b = b, a + b
        steps += 1
    return series, steps

def fibonacci_recursive(n, steps):
    steps[0] += 1
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1, steps) + fibonacci_recursive(n - 2, steps)

n = int(input("Enter the number of terms: "))

print("\n--- Non-Recursive Fibonacci ---")
start = time.time()
iterative_series, iterative_steps = fibonacci_iterative(n)
end = time.time()
print("Fibonacci Series:", iterative_series)
print("Steps Count:", iterative_steps)
print(f"Time taken: {end - start:.6f} seconds")
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")

print("\n--- Recursive Fibonacci ---")
steps = [0]
start = time.time()
recursive_series = [fibonacci_recursive(i, steps) for i in range(n)]
end = time.time()
print("Fibonacci Series:", recursive_series)
print("Steps Count:", steps[0])
print(f"Time taken: {end - start:.6f} seconds")
print("Time Complexity: O(2^n)")
print("Space Complexity: O(n)")
