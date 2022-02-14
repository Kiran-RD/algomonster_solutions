from typing import List

def find_min_rotated(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(arr)
    last_element = arr[-1]
    left, right = 0, n-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] <= last_element:
            right = mid
        else:
            left = mid+1
        
        if left == right:
            return mid

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = find_min_rotated(arr)
    print(res)