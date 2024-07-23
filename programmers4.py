# sorted() : iterable data를 새로운 정렬된 리스트로 만들어서 반환
# (data, key, reverse)
# key : 어떤 것을 기준으로 정렬할지 여부
# reverse : 오름차순(False), 내림차순(True)
# lambda x : 익명함수 (anonymous function) / 일회성 함수 => filter(), map(), sorted() 와 함께 사용
def solution(strings, n) :
    return sorted(strings, key=lambda x: (x[n], x))

