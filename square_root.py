def square_root(n: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    l, r = 0, n
    ans = -1
    while l <= r:
        k = (l+r)//2
        if k**2 == n:
            return k
        elif k**2 < n:
            ans = k
            l = k+1
        else:
            r = k-1
            
    return ans
        

if __name__ == '__main__':
    n = int(input())
    res = square_root(n)
    print(res)