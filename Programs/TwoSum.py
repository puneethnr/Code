#Given an array of integers and a value,
# determine if there are any two integers in the array whose sum is equal to the given value.

def twoSum(inputArray, givenNumber):

    arrayInDictionary = {}
    # Add array items into a dictionary
    for i in range(len(inputArray)):
        arrayInDictionary[i] = inputArray[i]
        difference = givenNumber - inputArray[i]
        if difference in arrayInDictionary.values():
            valueKey = getKey(arrayInDictionary, difference, i)
            if valueKey != None:
                return [i, valueKey]


def getKey(inputDictionary, valueToFind, notAcceptableKey):
    for key,value in inputDictionary.items():
        if value == valueToFind and key != notAcceptableKey:
            return key
    return None

print(twoSum([1,1,5,4], 2))