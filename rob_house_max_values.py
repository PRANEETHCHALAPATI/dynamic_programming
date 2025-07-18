def rob_house_max_value(houses,n,dp = {}):
    
    if n == -1:
        return 0 
    elif n == 0:
        return houses[0] 
    elif n == 1: 
        return max(houses[0],houses[1])
    
    else:
        if n not in dp:
            dp[n] = max(rob_house_max_value(houses,n-1,dp),rob_house_max_value(houses,n-2,dp) + houses[n]) 
        return dp[n]  
if __name__ == "__main__":
    houses = list(map(int, input("Enter the values of the houses separated by space: ").split()))
    max_value = rob_house_max_value(houses,len(houses)-1)
    print(f"The maximum value that can be robbed is: {max_value}")