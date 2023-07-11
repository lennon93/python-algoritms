def merge_sort(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left, right = merge_sort(string[:mid]), merge_sort(string[mid:])
    return merge(left, right)


def merge(left, right):
    left_cursor, right_cursor = 0, 0
    merged = []

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged.append(left[left_cursor])
            left_cursor += 1
        else:
            merged.append(right[right_cursor])
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged.append(left[left_cursor])

    for right_cursor in range(right_cursor, len(right)):
        merged.append(right[right_cursor])

    return merged


def is_anagram(first_string, second_string):
    first = ''.join(merge_sort(first_string.lower()))
    second = ''.join(merge_sort(second_string.lower()))

    if first != second or first == '' or second == '':
        return (first, second, False)

    return (first, second, True)
