def permute(nums):
    if not nums:
        return [[]]
    
    ret = []
    for i, x in enumerate(nums):
        perms = permute(nums[:i] + nums[i+1:])
        ret += [[x] + p for p in perms]
    
    return ret
