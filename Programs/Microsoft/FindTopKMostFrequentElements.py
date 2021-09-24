import heapq


# Using bucket sort
def findTopKFrequentElements(inputArray, k):
    numberCount = {}
    for n in inputArray:
        numberCount[n] = 1 + numberCount.get(n, 0)

    countofNumbers = [[] for i in range(len(inputArray)+1)]

    for n, count in numberCount.items():
        countofNumbers[count].append(n)

    klargest = []
    for i in range(len(countofNumbers) - 1, 0, -1):
        for n in countofNumbers[i]:
            klargest.append(n)
            if len(klargest) >= k:
                return klargest

    return klargest
    # heap = heapq.heapify(countofNumbers)
    # print(heapq.nlargest(2, countofNumbers))

# Using Heap
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self,other):
        return self.key < other.key

def findTopKFrequentElementsHeap(inputArray, k):
    numberCount = {}
    for n in inputArray:
        numberCount[n] = 1 + numberCount.get(n, 0)

    countofNumbers = []

    for n, count in numberCount.items():
        heapq.heappush(countofNumbers, Node(count, n))

    klargest = heapq.nlargest(k, countofNumbers)
    klargestNums = []
    for node in klargest:
        klargestNums.append(node.value)

    return klargestNums


#print(findTopKFrequentElements([1,1,1,2,2,3], 2))
print(findTopKFrequentElementsHeap([1,1,1,2,2,3], 3))
