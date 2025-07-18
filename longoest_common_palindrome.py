def is_palindrome(s,i,j):
    return s[i:j+1] == s[i:j+1][::-1]

def longest_common_palindrome(s,i,j,mem={}):
    if i>j:
        return ""
    if (i,j) in mem:
        return mem[(i,j)]
    else:
        if is_palindrome(s,i,j):
            mem[(i,j)] = s[i:j+1]
            return mem[(i,j)] 
        else:
            left = longest_common_palindrome(s,i,j-1,mem) 
            right = longest_common_palindrome(s,i+1,j,mem) 
            mem[(i,j)] = left if len(left) > len(right) else right
            return mem[(i,j)]  
def main():
    s = input("Enter a string:")
    n = len(s)
    result = longest_common_palindrome(s,0,n) 
    print(result)
if __name__ == "__main__":
    main()