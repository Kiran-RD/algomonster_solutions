from typing import List

def peak_of_mountain_array(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, len(arr)-1
    boundry = -1
    while left <= right:
        mid = (left+right)//2
        if mid == 0 or arr[mid] > arr[mid-1]:
            boundry = mid
            left = mid+1
        else:
            right = mid-1
           
    return boundry

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = peak_of_mountain_array(arr)
    print(res)