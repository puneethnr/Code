'''
Given a string str, the task is to find the lexicographically smallest string that can be formed by removing at most one character from the given string.
'''
def smallest_string(s: str) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    if str is '':
        return ''
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            break
    return s[:i] + s[i + 1:]