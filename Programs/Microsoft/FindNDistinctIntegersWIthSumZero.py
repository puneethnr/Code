def findNumbers(N):
    for i in range(1, N // 2 + 1):
        # Print 2 symmetric numbers
        print(i, end=', ')
        print(-i, end=', ')

    # Print a extra 0 if N is odd
    if N % 2 == 1:
        print(0, end='')


# Driver code
if __name__ == '__main__':
    N = 10
    findNumbers(N)