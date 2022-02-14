from typing import List

def binary_search(arr: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, len(arr)-1
    while left < right:
        mid = (left+right)//2
        if arr[mid]:
            right = mid
        else:
            left = mid+1
    
    if left==right and arr[left]:
        return left
    else:
        return -1

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = binary_search(arr, target)
    print(res)
