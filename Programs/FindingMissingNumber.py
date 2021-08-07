#You are given an array containing ‘n’
# distinct numbers taken from the range 0 to ‘n’.
# Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

def findMissingNumber(inputArray, n):
    numberExists = {}
    for i in range(n):
        numberExists[i] = False

    for i in inputArray:
        numberExists[i] = True
    print(numberExists)
    for number, Exists in numberExists.items():
        if Exists == False:
            return number

    return False


missingNumber = findMissingNumber([0,1,2,5,4], 5)
print(missingNumber)