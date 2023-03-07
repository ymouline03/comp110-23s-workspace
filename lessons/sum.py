def sum(sum_list: list[float]) -> float:
    '''returns sum of nums in  a list'''
    sum_total: float = 0
    for index in range(0, len(sum_list)):
        sum_total += sum_list[index]
    return sum_total

