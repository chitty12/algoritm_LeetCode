# 기다리는 사람 수 n
# 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 []
# 모든 사람이 심사 받는데 걸리는 시간 최솟값 return


def solution(n, times):
    low = 1
    high = max(times) * n
    
    while low <= high:
        mid = (low + high) // 2
        total = sum(mid // time for time in times)
        
        if total >= n:
            high = mid - 1
        else:
            low = mid + 1
            
    return low