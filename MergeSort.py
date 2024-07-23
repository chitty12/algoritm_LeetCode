# 6, 1, 4, 9, 2, 5, 8, 7
import math

class MergeSort :
    def __init__(self, array):
        self.array = array
        self.divided_array = []
        
        
    def divide_array(self, array):
        length = len(self.array)
        if len(array) == 1:
            return self.divided_array.append(array)
        else:
            new_array = []
            new_array2 = []
            for i in range(array[math.floor(length/2)]):
                new_array.append(array[i])
            for i in range(array[math.floor(length/2)+1 : length-1]):
                print('i', i)
                new_array2.append(array[i])
            print(new_array)
            print(new_array2)

            self.divide_array(new_array)
            self.divide_array(new_array2)
                
                
                
                
                
ex = MergeSort([6, 1, 4, 9, 2, 5, 8, 7])


new_arr = ex.divide_array(ex.array)

print(new_arr)