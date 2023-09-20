def find_duplicate(nums):
    array = []

    for num in nums:

        if type(num) != int or num < 0:
            return False

        # if nums.count(num) > 1:
        #     return num

        if num in array:
            return num

        array.append(num)

    return False
