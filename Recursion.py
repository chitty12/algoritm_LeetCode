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
        if balls == self.share:
            self.count += 1
            return self.count
        else:
            count = self.Factorial(balls) // (self.Factorial(self.share) * self.Factorial(balls - self.share))
            self.count += count
            self.share += 1
            return self.BallCount(balls)


    def Factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.Factorial(n - 1)




DivideBallCount = solution(5)
totalCount = DivideBallCount.BallCount(5)

print(totalCount)