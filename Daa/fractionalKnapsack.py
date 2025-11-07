def fractionalKnapsack(values, weights, capacity):
    n = len(values)
    items = []
    for i in range(n):
        item = [values[i], weights[i], i]
        items.append(item)

    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0.0
    current_capacity = capacity
    fractions = [0.0] * n

    for v, w, idx in items:
        if w <= current_capacity:
            total_value += v
            current_capacity -= w
            fractions[idx] = 1.0
        else:
            fraction = current_capacity / w
            total_value += v * fraction
            fractions[idx] = fraction
            break

    return total_value, fractions


n = int(input("Enter number of items: "))
values = []
weights = []

for i in range(n):
    v = float(input(f"Enter value of item {i+1}: "))
    w = float(input(f"Enter weight of item {i+1}: "))
    values.append(v)
    weights.append(w)

capacity = float(input("Enter capacity of the knapsack: "))

max_value, fractions = fractionalKnapsack(values, weights, capacity)

print(f"\nMaximum value: {max_value:.2f}")
for i in range(n):
    print(f"Item {i+1}: {fractions[i]:.2f}")