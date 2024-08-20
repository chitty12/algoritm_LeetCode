# set : 중복 불가 / 가장 최신의 데이터로 덮어씌움
# get : key값에 대한 value 값 가져오기

class Node :
    def __init__(self, item, link):
        self.item = item,
        self.link = link
        
        
class HashTable :
    def __init__(self, length = 5):
        self.max_len = length
        self.table = [[] for _ in range(self.max_len)]

# ord(a) : 문자의 순서 위치 값(unicode)로 변환
# <=> chr(12) : 정수값을 유니코드 문자로 변환
    def _hash(self, key):
        res = sum([ord(s) for s in key])
        return res % self.max_len

    def set(self, key, value):
        index = self._hash(key)
        if not self.get(key):
            self.table[index][key] = value
        else:
            self.table[index].append((key, value))
        
    def get(self, key):
        index = self._hash(key)
        value = self.table[index]
        if not value:
            return None
        for v in value:
            if v[0] == key:
                return v[1]
        return None