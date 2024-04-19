# 스택 구현하기
# 생성자에 최소한 size, arr 를 포함한 2개 이상을 사용할 것
# js에서 제공하는 push, pop 메서드 쓰지 않고 push, pop 메서드 만들것
# push나 pop에서 size가 10개를 넘어가거나 음수를 향할 경우 overflow, underflow같은 예외 처리사항 조건 달기
# 만들어야 하는 메서드
# push : 스택에 해당하는 후입에 해당하는 넣는 기능
# pop : 스택에 해당하는 선출에 해당하는 빼는 기능
# peek : 스택의 현재 배열을 출력
# isEmpty : 스택이 현재 비어있는지 확인하는 기능
# getSize : 스택의 현재 사이즈를 확인
# maxSize 를 설정하는 방법 Good!!!!


class stack ():
    def __init__(self):
        self.arr = [],
        self.size = 0

    def push (self, item):
        if self.size <= 10:
            self.arr.append(item)
            self.size += 1
            return 
        else:
            print('stack is overflow')
        
    def pop (self):
        if self.size != 0:
            del self.arr[-1]
            self.size -= 1
        else:
            print('stack is underflow')

    def peek (self):
            print(self.arr)
        
    def isEmpty (self):
        if self.size == 0:
            print('stack is empty')
    
    def getSize (self):
        print("current stack size is %d" %self.size)



# 1. 생성자에 최소한 size, arr를 포함한 2개 이상을 사용할 것
# 2. js에서 제공하는 기본 메서드가 아닌 enqueue, dequeue 메서드를 작성할 것
# 3. size가 10개를 넘어가거나 음수를 향할 경우 overflow, underflow같은 예외 처리사항 조건 달기

# 만들어야 하는 메서드
# enqueue : 선입에 해당하는 push 기능
# dequeue : 선출에 해당하는 pop 기능
# peek : 큐의 현재 배열을 출력
# isEmpty : 큐가 현재 비어있는지 확인하는 기능
# getSize : 큐 현재 사이즈를 확인
# getRear : 큐의 현재 rear에 해당하는 value값 출력
# getFront :  큐의 현재 front에 해당하는 value값 출력

class queue ():
    def __init__(self):
        self.arr = []
        self.size = 0
        self.maxSize = 10
        self.rear = 0
        self.front = 0

    def enqueue(self, item):
        if self.size < self.maxSize:
            self.arr.append(item)
            self.size += 1
            self.rear += 1
        else:
    
    def dequeue(self, index):




# leetcode 641번 문제 풀어오기(design circular deque)