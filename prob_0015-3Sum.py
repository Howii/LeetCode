from collections import defaultdict

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    out = []
    pos_dict = defaultdict(int)
    neg_dict = defaultdict(int)
    num_zeros = 0
    for x in nums:
        if x == 0:
            num_zeros += 1
        elif x > 0:
            pos_dict[x] += 1
        elif x < 0:
            neg_dict[x] += 1
    
    # [0, 0, 0]
    if num_zeros >= 3:
        out.append([0, 0, 0])

    # [pos, 0, neg]
    if num_zeros > 0:
        for p in pos_dict:
            if -p in neg_dict:
                out.append([p, 0, -p])
    # [pos, neg, neg]
    for p in pos_dict:
        for n in neg_dict:
            m = - p - n
            if (m in neg_dict and
                (m > n or (m == n and neg_dict[m] > 1))):
                out.append([n, m, p])
    # [pos, pos, neg]
    for n in neg_dict:
        for p in pos_dict:
            q = - n - p
            if (q in pos_dict and
                (p < q or (p == q and pos_dict[q] > 1))):
                out.append([p, q, n])
    return out
