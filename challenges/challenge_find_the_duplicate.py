from collections import defaultdict


def find_duplicate(nums):
    array = defaultdict(lambda: 0)

    for num in nums:

        if type(num) != int or num < 0:
            return False

        array[num] += 1

        if array[num] > 1:
            return num

    return False
