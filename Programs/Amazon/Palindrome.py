# function to check string is
# palindrome or not
def isPalindrome(str):
    # Run loop from 0 to len/2
    stringLength = len(str)
    for i in range(0, int(stringLength / 2)):
        if str[i] != str[stringLength - i - 1]:
            return False
    return True


# main function
s = "malayalam"
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")


# very easy in Python
# s[::-1] reverses a string in Python
def isPalindrome(s):
    return s == s[::-1]


# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")