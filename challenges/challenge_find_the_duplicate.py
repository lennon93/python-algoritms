def find_duplicate(nums):   
    if len(nums) < 2:
        return False
    
    for i in nums:
        if not isinstance(i, int):
            return False
        if i < 1:
            return False
        number = i
        nums.pop(nums.index(i))    
        if number in nums:
            return number
    return False