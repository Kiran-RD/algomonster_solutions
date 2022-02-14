from typing import List

def sort_list(unsorted_list: List[int]) -> List[int]:
    
    for i in range(len(unsorted_list)):
        min_idx = i
        for j in range(i,len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[min_idx]:
                min_idx = j
        unsorted_list[i], unsorted_list[min_idx] = unsorted_list[min_idx], unsorted_list[i]
            
    
    return unsorted_list

if __name__ == '__main__':
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(' '.join(map(str, res)))
