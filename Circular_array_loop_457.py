# 처음 시작하는 인덱스번호 = t
# 순회 i
# 숫자 추출 => i + k = index
# length <= i+k => i+k - length
# i + k < 0 => length - (k - i)
# if t = i 가 되는 때 true
# 다음 인덱스가 i 일때 false


class CircularArrayLoop :
    def __init__(self, startIndex, ):
        self.startIndex = startIndex

    def Solution (self, circularArray):

        for in circularArray:
            if(circularArray.length <= ):
                return 