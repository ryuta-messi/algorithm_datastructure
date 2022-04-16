from typing import List
import random

def bobble_sort(numbers:List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers -1 -i):
            if numbers[j] > numbers[j+1]:
                numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
    return numbers


if __name__ == '__main__':
    nums = [random.randint(1,1000) for _ in range(20)]
    print(bobble_sort(nums))


