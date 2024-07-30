def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    arr = sorted(nums1 + nums2)
    n = len(arr)
    if n % 2 == 0:
       median = (arr[(n // 2) - 1] + arr[n // 2]) / 2
    else:
        median = arr[n // 2] 
    return median

if __name__ == '__main__':
    with open('user.out', 'w') as f:
        for nums1, nums2 in zip(map(loads, stdin), map(loads, stdin)):
            result = findMedianSortedArrays(nums1, nums2)
            print(f'{result}', file=f)
        exit()