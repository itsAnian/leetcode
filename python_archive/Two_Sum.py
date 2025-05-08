def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    for i in range(len(nums)):
        for ii in range(len(nums)):
            tmp = nums[i] + nums[ii]
            if(tmp == target and i != ii):
                result = [i, ii]
                return result
    return []

def main():
    nums = [3,2,4]
    target = 6
    print(twoSum(nums, target))

main()
