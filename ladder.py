def ladder(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 2:
        return n
    if n not in memo:
        memo[n] = ladder(n - 1, memo) + ladder(n - 2, memo)
    return memo[n]

if __name__ == "__main__":
    N = int(input(f"\nEnter the number of steps: ")) 
    print(f"\nNumber of distinct ways to climb {N} steps: {ladder(N)}")
    print("\nYou can climb either 1 or 2 steps at a time. This program uses dynamic programming to efficiently calculate all unique climbing combinations.")
