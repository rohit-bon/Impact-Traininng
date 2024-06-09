def knapsack(wt, val, W, n):
    # base condition 
    if n==0 or W==0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
    
    # choice diagram code 
    if wt[n-1] <= W:
        t[n][W] = max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1))
        return t[n][W]
    elif wt[n-1] > W:
        t[n][W] = knapsack(wt, val, W, n-1)
        return t[n][W]

if __name__ == '__main__':
    profit = [1, 2, 3]
    weight = [4, 5, 1]
    W = 4
    n = len(profit)

    # we initialize  the matrix with -1 at first 
    t = [[-1 for i in range(W + 1)] for j in range(n+1)]
    print(knapsack(weight, profit, W, n))