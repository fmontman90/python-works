nums = [3,1,2,10,1]
nums2 = [1,1,1,1,1]
#output num1 should be 3,4,6,16,17
#To start we need to go through an array with a for loop 

def runningsum(nums:[int]):
    ans = [] #This array will kepp track of ans
    for i in range(len(nums)): #iterate thorugh all the elements in nums
        runningsum = 0 #This will keep track of the running sum up to index i
        for j in range(i +1):
            runningsum += nums[j] #sum all the elements leading up to nums[i]
        ans.append(runningsum) # add the sum to our answer array
    return ans

print(runningsum(nums))
print(runningsum(nums2))