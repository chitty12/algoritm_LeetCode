# 선형탐색
# 이분탐색
import math


def linear_search(arr, x):
    # enumerate() : list, set, dictionary, string 입력받을 때, 인덱스 및 값을 포함하여 리턴해 줌
    for i, value in enumerate(arr):
        if value == x:
            return i
    return -1


def binary_search(arr, x):
    start = 0            # 맨 처음 위치
    end = len(arr) - 1   # 맨 마지막 위치
    
    while start <= end:
        mid = math.floor((start + end) / 2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return -1