def sort_string(string):
    if string == '':
        return ''

    sorted = list(string.lower())
    length = len(sorted)

    for index in range(length):

        for index2 in range(index + 1, length):
            if sorted[index2] < sorted[index]:

                sorted[index], sorted[index2] = sorted[index2], sorted[index]

    return ''.join(sorted)


def is_anagram(first_string, second_string):
    first = sort_string(first_string)
    second = sort_string(second_string)

    if first != second or first == '' or second == '':
        return (first, second, False)

    return (first, second, True)
