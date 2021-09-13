# Given a 2D matrix of 0s and 1s, find total number of clusters formed by elements with value 1
# While modeling the 'matrix' as a graph -
# 1. An element matrix[i][j] with value 1 is considered as a vertex.
# 2. All adjacent elements of matrix[i][j] with value 1 are considered as its neighbor vertices. An element can have maximum of eight neighbors as shown below.
# With this graph modeling in place, we use following algorithm to find total number of clusters -
# 1. Initialize count to 0. Initialize a 2D 'visited' array of booleans which is of size equal to given matrix. Initialize all elements of 'visited' array to false.
# 2. For an element matrix[i][j], if matrix[i][j] is '1' and visited[i][j] is 'false' then
# 2a. Increment count by 1.
# 2b. Start depth first search from element matrix[i][j]. Along with element matrix[i][j], this depth first search would mark all the vertices which are directly or indirectly connected to element matrix[i][j] as visited. In short all the vertices in the cluster starting from vertex matrix[i][j] are visited in this depth first search.
# 3. Repeat step #2 for all the elements of given 2D matrix.
# 4. Return the 'count' which is basically total number of clusters of 1s in given 2D matrix.

def numberOfIslands(inputMatrix):

    #Create a new boolean representation of the matrix
    visitedMatrix = []
    row, column = 0, 0
    count = 0
    for listOfNumbers in inputMatrix:
        currentRow = []
        column = 0
        for number in listOfNumbers:
            currentRow.insert(column,False)
            column = column + 1
        visitedMatrix.insert(row, currentRow)
        row = row + 1
    print(visitedMatrix)


    for i in range(len(inputMatrix)):
        for j in range(len(inputMatrix[i])):
            if (inputMatrix[i][j] == 1 and not(visitedMatrix[i][j])):
                count = count + 1
                doDFS(inputMatrix, i ,j, visitedMatrix)

    return count

def doDFS(inputMatrix, i , j, visitedMatrix):
    if(visitedMatrix[i][j]):
        # If node has already been visited return.
        return

    # Mark the node passed in as visited and do a depth first search of remaining nodes
    visitedMatrix[i][j] = True
    offsets = [-1, 0, 1]
    for m in offsets:
        for n in offsets:
            if m == 0 and n == 0:
                continue

            if neighbourExists(inputMatrix, i + m, j + n):
                doDFS(inputMatrix, i + m, j + n, visitedMatrix)

def neighbourExists(inputMatrix, row, column):
    if row >= 0 and row < len(inputMatrix) and column >= 0 and column < len(inputMatrix[0]):
        if inputMatrix[row][column] == 1:
            return True

    return False


islandCount = numberOfIslands([ [1,0,1],
                                [0,0,1],
                                [1,0,1]
                              ]
                            )

print(islandCount)


