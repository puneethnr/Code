'''
ou are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0
'''

def findMaxProfit(inputArray):

    left,right = 0,1 #left = buy, right = sell
    maxProfit = 0
    while right < len(inputArray):
        # Is profitable?
        currentProfit = inputArray[right] - inputArray[left]
        if currentProfit > 0:
            maxProfit = max(maxProfit, currentProfit)
        else:
            left = right
        right += 1
    return maxProfit

def findreturnMaxProfitDays(inputArray):

    left,right = 0,1 #left = buy, right = sell
    maxProfit = 0
    sellDate, buyDate = 0, 0
    while right < len(inputArray):
        # Is profitable?
        currentProfit = inputArray[right] - inputArray[left]
        if currentProfit > 0:
            if  currentProfit > maxProfit:
                buyDate = left
                sellDate = right
                maxProfit = currentProfit
        else:
            left = right
        right += 1
    return [buyDate, sellDate]

print(findMaxProfit([7,1,5,3,6,4]))
print(findreturnMaxProfitDays([7,1,5,3,6,4]))

