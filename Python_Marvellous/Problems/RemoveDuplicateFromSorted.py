def removeDuplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[j] == nums[i]:
            i += 1
            nums[i] = nums[j]
        
    return i 

print(removeDuplicates([1,1,2,3]))