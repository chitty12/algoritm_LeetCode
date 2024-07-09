def solution_recursive(a, b, n, total_colas=0):
    if n < a:
        return total_colas

    new_colas = (n // a) * b
    # 남은 빈 병
    new_empty_bottles = (n % a) + new_colas
    # 총 콜라 병
    total_colas += new_colas

    return solution_recursive(a, b, new_empty_bottles, total_colas)

result = solution_recursive(3, 1, 20)
print(result)
 