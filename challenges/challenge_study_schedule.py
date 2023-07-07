def study_schedule(permanence_period, target_time):
    count = 0
    if target_time == None:
        return None
    if not isinstance(permanence_period, list) or not all(isinstance(item, tuple) and all(isinstance(num, int) for num in item) for item in permanence_period):
        return None
    for item in permanence_period:
        if item[0] <= target_time <= item[1]:
            count += 1
    return count
