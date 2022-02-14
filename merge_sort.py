from typing import List
def sort_list(unsorted_list: List[int]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(unsorted_list)
    if n <= 1:
        return unsorted_list
    midpoint = n // 2
    left_list, right_list = sort_list(unsorted_list[:midpoint]), sort_list(unsorted_list[midpoint:])
    result_list = []
    left_pointer, right_pointer = 0, 0
    while left_pointer < midpoint or right_pointer < n - midpoint:
        if left_pointer == midpoint:
            result_list.append(right_list[right_pointer])
            right_pointer += 1
        elif right_pointer == n - midpoint:
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        elif left_list[left_pointer] <= right_list[right_pointer]:
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result_list.append(right_list[right_pointer])
            right_pointer += 1
    return result_list            

if __name__ == '__main__':
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(' '.join(map(str, res)))