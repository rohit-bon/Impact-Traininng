def remove_consecutive_duplicates(s):
    result = []
    for char in s:
        if len(result) == 0 or char != result[-1]:
            result.append(char)
    return ''.join(result)

s = input()
print(remove_consecutive_duplicates(s))
