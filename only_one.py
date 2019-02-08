
def removeDuplicates(nums):
    nums_dict = {}
    for i in nums:
        if nums_dict.get(i) is None:
            nums_dict[i] = 1
        else:
            nums_dict[i] +=1
    for k,v in nums_dict.items():
        if v>=2:
            for i in range(v-1):
                nums.remove(k)
    return len(nums)
nums = [ 1,1,1,1,2,2,2]
print(removeDuplicates(nums))