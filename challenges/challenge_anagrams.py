def sort_string(string):
    if string == '':
        return ''

    list_string = list(string.lower())
    length = len(list_string)

    for index in range(length):

        for index_two in range(index + 1, length):
            if list_string[index_two] < list_string[index]:

                list_string[index] = list_string[index_two]
                list_string[index_two] = list_string[index]

    return ''.join(list_string)


def is_anagram(first_string, second_string):
    first = sort_string(first_string)
    second = sort_string(second_string)

    if first != second or first == '' or second == '':
        return (first, second, False)

    return (first, second, True)
