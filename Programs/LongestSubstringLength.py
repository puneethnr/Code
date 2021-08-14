# Given a string str, find the length of the longest substring without repeating characters.
#
# For “ABDEFGABEF”, the longest substring are “BDEFGA” and “DEFGAB”, with length 6.
# For “BBBB” the longest substring is “B”, with length 1.
# For “GEEKSFORGEEKS”, there are two longest substrings shown in the below diagrams, with length 7


def longestSubstringLength(inputString):
    i, j, maxLength = 0, 0, 0
    characterSet = set()
    for eachCharacter in inputString:
        if not eachCharacter in characterSet:
            characterSet.add(eachCharacter)
            j = j + 1
            maxLength = max(len(characterSet), maxLength)
        else:
            characterSet.remove(eachCharacter)
            i = i + 1
    return maxLength

print(longestSubstringLength("abdefgabef"))


