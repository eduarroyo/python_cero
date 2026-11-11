def average(*numbers: float):
    return sum(numbers)/len(numbers)

def median(*numbers: float):

    length = len(numbers)
    if length == 0:
        return None

    middle_index = length // 2
    sorted_list = list(numbers)
    sorted_list.sort()
    if length % 2 == 0:
        return (sorted_list[middle_index-1] + sorted_list[middle_index])/2
    else:
        return sorted_list[middle_index]
