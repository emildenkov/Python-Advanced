def palindrome(word, index):

    if index == len(word) // 2:
        return f"{word} is a palindrome"

    if word[index] != word[-index - 1]:
        return f"{word} is not a palindrome"

    result = palindrome(word, index + 1)

    return result


print(palindrome("abcba", 0))
