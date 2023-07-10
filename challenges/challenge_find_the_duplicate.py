def find_duplicate(nums):
    number_set = set()

    for number in nums:
        if not isinstance(number, int) or number < 1:
            return False

        if number in number_set:
            return number

        number_set.add(number)

    return False
