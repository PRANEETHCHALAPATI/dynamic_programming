def fib(n,memo={}):
    if n<=1:
        return n 
    else:
        if n not in memo:
            memo[n] = fib(n-1,memo)+fib(n-2,memo) 
        return memo[n] 

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"The {n}th Fibonacci number is: {fib(n)}")