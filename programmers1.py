def solution(s, answer = None):
    if answer is None:
        answer = [0, 0]

    if s == "1":
        return answer
    else :
        new_number_str = ''
        count = 0
        for i in s:
            if i != '0':
                new_number_str += i
            else:
                count += 1        
        new_number = bin(len(new_number_str))[2:]

        answer[0] += 1
        answer[1] += count

        print(answer)
        print(str(new_number))

        return solution(str(new_number), answer)