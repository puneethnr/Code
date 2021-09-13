# Given a string str, find the length of the longest substring without repeating characters.
#
# For “ABDEFGABEF”, the longest substring are “BDEFGA” and “DEFGAB”, with length 6.
# For “BBBB” the longest substring is “B”, with length 1.
# For “GEEKSFORGEEKS”, there are two longest substrings shown in the below diagrams, with length 7


def longestSubstringLength(inputString: str) -> int:

    maxLength = 0
    charDictionary = {}
    current_sub_start = -1
    currentSubstrnLength = 0
    for i, eachCharacter in enumerate(inputString):
        if eachCharacter in charDictionary and charDictionary[eachCharacter] >= current_sub_start:
            current_sub_start = charDictionary[eachCharacter] + 1
            currentSubstrnLength = i - charDictionary[eachCharacter]
            charDictionary[eachCharacter] = i
        else:
            charDictionary[eachCharacter] = i
            currentSubstrnLength += 1
            maxLength = max(currentSubstrnLength, maxLength)
    return maxLength

print(longestSubstringLength("aab"))


