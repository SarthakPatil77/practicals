def knapsack_dp(weights, values, capacity):
   n = len(weights)
   dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
   for i in range(1, n + 1):
       for w in range(1, capacity + 1):
           if weights[i - 1] <= w:
               dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
           else:
               dp[i][w] = dp[i - 1][w]

   w = capacity
   selected_items = []
   for i in range(n, 0, -1):
       if dp[i][w] != dp[i - 1][w]:
           selected_items.append(i - 1)
           w -= weights[i - 1]

   return dp[n][capacity], selected_items[::-1]

def main():
   n = int(input("Enter the number of items: "))

   weights = []
   values = []

   for i in range(n):
       w = int(input(f"Enter weight of item {i+1}: "))
       v = int(input(f"Enter value of item {i+1}: "))
       weights.append(w)
       values.append(v)

   capacity = int(input("Enter the capacity of the knapsack: "))

   max_value, items = knapsack_dp(weights, values, capacity)
   print("\nDP Solution:")
   print("Maximum value:", max_value)
   print("Items included (0-based indices):", items)

main()