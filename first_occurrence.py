from typing import List

def find_first_occurrence(arr: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    l, r = 0, len(arr)-1
    idx = -1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == target:
            idx = mid
            r = mid-1
        elif target < arr[mid]:
            r = mid-1
        else:
            l = mid+1
    return idx
           
               
if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = find_first_occurrence(arr, target)
    print(res)