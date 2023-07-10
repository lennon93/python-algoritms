def is_palindrome_iterative(word):
    if not word:
        return False

    create_list = list(word.lower())[::-1]
    reversed_word = "".join(create_list)

    if word.lower() == reversed_word:
        return True
    return False
