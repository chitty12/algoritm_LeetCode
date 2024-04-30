# 머쓱이의 구슬 나누기
# 구슬의 개수 balls
# 나누어 줄 구슬 개수 share
# balls 구슬 중 share 개의 구슬을 고르는 가능한 모든 경우의 수 return

class solution:
    def __init__(self, balls, share = 1, count = 0):
        self.balls = balls
        self.share = share
        self.count = count
    
    def BallCount(self, balls):
        
        if(self.balls == self.share):
            return self.count

        else:
            totalBall = self.Factorial(balls)
            count = totalBall/(self.Factorial(self.share))
            self.count += count
            self.share +=1
            return self.BallCount(balls-1)



    def Factorial(self, number, countNumber):
        if( counts == countNumber):
            return counts
        elif(number == 1):
            return 1
        elif(number == 0):
            return 1
        else:
            count = number*(self.Factorial(number-1, countNumber))
            return count




DivideBallCount = solution(5)

factorial = DivideBallCount.Factorial(4)

totalCount = DivideBallCount.BallCount(5)


print(factorial)
print(totalCount)