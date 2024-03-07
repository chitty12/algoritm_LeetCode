

def is_sorted(arr):
# 배열의 길이가 1 이하인 경우는 항상 정렬되어 있다고 간주
    if len(arr) <= 1:    
        return True
# 배열을 순회하면서 non decreasing order 으로 정렬되어 있는지 확인
# [i+1]의 값이 [i]보다 작음 : False / 큼 : True / 값이 같을 경우 : True
# 모든 i에 대해 만족해야 return True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
        return True
    
    # 1인지 여부 확인 : 상수
    # 반복문 n * 비교연산 (상수) : n
    # 시간복잡도 O(n)