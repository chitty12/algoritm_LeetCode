# 버블정렬

sample_list = [32, 5, 40, 11, 8, 45, 100, 1]
# len() : 크기
# range(N) : 0 ~ N-1 까지의 리스트를 만들어주는 함수

def BubbleSort(list) :
    unsorted = 0

    for i in range(len(list)):
        if len(list) != i + 1 :
            if list[i] > list[i+1]:
                a = list[i]
                b = list[i+1]
                list[i] = b
                list[i+1] = a
            else :
                unsorted += 1

    if (unsorted+1) == len(list):
        return print(list)
    else : 
        BubbleSort(list)


print(BubbleSort(sample_list))



sample_list = [32, 5, 40, 11, 8, 45, 100, 1]
# 삽입정렬
def InsertSort(list):
    for i in range(len(list)):
        list[i+1]
        





print(InsertSort(sample_list))