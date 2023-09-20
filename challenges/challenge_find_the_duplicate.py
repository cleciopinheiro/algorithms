def find_duplicate(nums):
    array = set()
    for num in nums:

        if type(num) != int or num < 0:
            return False

        if num in array:
            return num

        array.add(num)

    return False
