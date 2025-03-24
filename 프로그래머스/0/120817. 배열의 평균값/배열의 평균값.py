def solution(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum / len(numbers)