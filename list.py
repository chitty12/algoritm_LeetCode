# is_empty(): O(1)
# prepend(): O(n)
# append(): O(n) (조건부 O(1))
# set_head(index): O(1)
# access(index): O(1)
# insert(item, index): O(n)
# remove(index): O(n)

class List:
    def __init__(self):
        self.list = []
        self.size = 0
        self.maxSize = 10

    def is_empty(self):
        if(self.size == 0):
            return True
        else:
            return False

    def prepend(self, item):
        if(self.size <= self.maxSize):
            self.list=[item, ...]
            self.size += 1
            return self.list
        else:
            return False
        
    def append(self, item):
        if(self.size == 0):
            self.list = [item]
            self.size = 1
            return self.list
        if(0< self.size <= self.maxSize):
            self.list = self.list + [item]
            self.size += 1
            return self.list
        else:
            return False
    
    def access(self, index):
        if(index < self.size):
            return self.list[index]
        else:
            return False
    
    def insert(self, item, index):
        if(self.size >= index):
            self.list[index] = item
            return self.list
        else:
            return False
    
    def remove(self, index):
        if(0 <= index < self.size):
            self.list = self.list[:index-1] + self.list[index+1:]
            # delete 메서드
            self.size -= 1
            return self.list
        else:
            return False



my_list = List()

print(my_list.is_empty())
print(my_list)
print(my_list.append(1))
print(my_list.append(2))
