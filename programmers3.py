def solution(array, commands):
    result = []
    for command in commands:
        new_array=[]
        if command[0] == command[1]:
            result.append(array[command[0]-1])
        else:
            for i in range(command[1]):
                new_array.append(array[i])
            if command[0] == 1:
                new_array.sort()
                result.append(new_array[command[2]-1])
            else: 
                for j in range(command[0]-1):
                    del new_array[j]
                    new_array.sort()
                result.append(new_array[command[2]-1])
    return result



ex_array = [1, 5, 2, 6, 3, 7, 4]
ex_commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(ex_array, ex_commands))