#Given an array of integers and a value,
# determine if there are any two integers in the array whose sum is equal to the given value.

def twoSum(inputArray, givenNumber):

    arrayInDictionary = {}
    # Add array items into a dictionary
    for i, n in enumerate(inputArray):

        difference = givenNumber - inputArray[i]
        if difference in arrayInDictionary.keys():
            return [arrayInDictionary[i], i]
        arrayInDictionary[n] = i

print(twoSum([1,1,5,4], 2))