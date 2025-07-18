def knapsack(n,weights,values,target,dp={}):
    if n == len(weights) or target <= 0:
        return 0 
    else:
        if (n,target) not in dp:
            include = 0 
            if weights[n] <= target:
                include = values[n]+knapsack(n+1,weights,values,target-weights[n],dp) 
            exclude = knapsack(n+1,weights,values,target,dp) 
            dp[(n,target)] = max(include, exclude) 
        return dp[(n,target)] 
def main():
    n = int(input("Enter number of items:"))
    weigths = list(map(int,input("Enter Weights:").split())) 
    
    values = list(map(int,input("Enter Values:").split())) 
    
    target = int(input("Enter Maximum Weight:"))
    
    if len(weigths) != n or len(values) != n:
        print("Error: Number of weights and values must match the number of items.")
        return 
    result = knapsack(0, weigths, values, target) 
    print("Maximum value in Knapsack =", result) 
if __name__ == "__main__":
    main()