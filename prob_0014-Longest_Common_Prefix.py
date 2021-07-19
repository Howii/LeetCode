def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]
    N = min([len(x) for x in strs])
    i = 0
    while i < N:
        if len(set([x[i] for x in strs])) > 1:
            break
        i += 1
    return strs[0][0:i]
