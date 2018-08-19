# ---------------------------------------#
# Qishi algorithm group - homework 1.    #
# -------------------------------------- #

## Q1: Best Time to Buy and Sell Stock. (LC121)
'''
method 1
First calculate the cumulative price increment and set 0 if become negative
Second calculate the maximum increment price over the time
'''
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxcur = 0
        maxall = 0
        for i in range(1,len(prices)):
            maxcur+=prices[i]-prices[i-1]
            maxcur = max(0,maxcur)
            maxall = max(maxcur,maxall)
        return maxall
'''
Method 2
Assume i don't have money but i can borrow money to buy stock.
for every loop, it will look up the lowest buy in price and compare the difference
between the previous max profit and the current profit to find the overall maximum profit
'''
import math as math
class Solution:
    def maxProfit(self, prices):
    	buy = -math.inf
    	sell = 0
    	for price in prices:
    		buy=max(buy,-price)
    		sell=max(sell,price+buy)
    	return sell

## Q2: Best Time to Buy and Sell Stock II (LC 122)

'''
record the positive difference between two adjacent points and the cumulative
difference is the max profit
'''
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        for i in range(0,len(prices)-1):
            if prices[i+1]-prices[i]>0:
                maxprofit += prices[i+1]-prices[i]
        return maxprofit


## Q3: Best Time to Buy and Sell Stock III (LC 123)
'''
utilize the similar idea from method 2 in Q1
buy1 and sell1 are related to the first transaction
buy2 and sell2 are related to the second transaction
sell1 is the maximum profit for the first transaction before the point in time
based on sell1, sell2 is the maximum profit for two transaction before the point in time
return sell2
'''

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1=buy2=-math.inf
        sell1=sell2=0
        for price in prices:
            sell2 = max(sell2,buy2+price)
            buy2 = max(buy2,sell1-price)
            sell1 = max(sell1,buy1+price)
            buy1 = max(buy1,-price)
        return sell2

## Q4: Find All Numbers Disappeared in an Array (LC 448)
'''
Method 1
for each number i in nums,
we mark the number that i points as negative.
then we filter the list and get all the indexes
who points to a positive number since those indexes are not visited
'''
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            ind = abs(nums[i])-1
            nums[ind] = -abs(nums[ind])
        return [i+1 for i in range(len(nums)) if nums[i]>0]

'''
Method 2
use the characteristics of set
'''
class Solution:
    def findDisappearedNumbers(self, nums):
    	return list(set(range(1,len(nums)+1))-set(nums))

## Q5: First Missing Positive (LC 41)
'''
set negative number as 0
use the characteristics of set and get the list 
stores the potentiual unique missing positive numbers
case 1: this list exists and min(list) will give the result
case 2: this list is empty and return len(nums)-1
'''
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=0
        mis = list(set(range(1,len(nums)+1))-set(nums))
        if mis:
            return min(mis)
        else:
            return len(nums)+1

## Q6: 4Sum (LC 18)
'''
first sort the list
second do the 3 loops and store the value target - nums[i]-nums[j]-nums[k] into temp
if continue looping and we can find nums[k] in temp then we can get one solution
be cautious to check the duplicates
'''
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums)<4:
            return []
        nums.sort()
        res=[]
        for i, a in enumerate(nums):
            if i>=1 and a==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-1):
                temp=set()
                for c in nums[j+1:]:
                    if c not in temp:
                        temp.add(target-a-nums[j]-c)
                    else:
                        x = sorted([a,nums[j],c,target-a-nums[j]-c])
                        if x not in res:
                            res.append(x)
        return res

## Q7: Majority Element II (LC 229)
'''
Boyer-Moore Majority Vote algorithm generalization
'''
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count1,count2,candidate1,candidate2=0,0,0,1
        res=[]
        for num in nums:
            if num==candidate1:
                count1+=1
            elif num==candidate2:
                count2+=1
            elif count1==0:
                candidate1,count1=num,1
            elif count2==0:
                candidate2,count2=num,1
            else:
                count1-=1
                count2-=1
        return [n for n in (candidate1,candidate2) if nums.count(n)>len(nums)//3]
            
## Q8: Set Matrix Zeroes (LC 73)
'''
Record the row and column indexes for zeros in the matrix
Fix every zero index and set zeros for the whole line
'''
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_zero = set()
        col_zero = set()
        m=len(matrix) # row number
        n=len(matrix[0]) # column number
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not matrix[i][j]:
                    row_zero.add(i)
                    col_zero.add(j)
        
        # for row_num, row in enumerate(matrix):
        #     for col_num, val in enumerate(row):
        #         if val==0:
        #             row_zero.add(row_num)
        #             col_zero.add(col_num)
        for row in row_zero:
            for col in range(n):
                matrix[row][col]=0
        for col in col_zero:
            for row in range(m):
                matrix[row][col]=0
