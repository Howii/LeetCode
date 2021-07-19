def oddHelper(s, k):
    """1 <= k <= n-2"""
    i = 1
    N = min(k, len(s) - 1 - k)
    while i <= N:
        if s[k - i] != s[k + i]:
            break
        else:
            i += 1
    return (1 + 2 * (i - 1), s[k - i + 1 : k + i])

def evenHelper(s, k):
    """1 <= i <= n-2"""
    if s[k] != s[k + 1]:
        return (0, '')
    i = 1
    N = min(k, len(s) - 2 - k)
    while i <= N:
        if s[k - i] != s[k + 1 + i]:
            break
        else:
            i += 1
    return (2 + 2 * (i - 1), s[k - i + 1 : k + i + 1])

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if len(s) == 1:
        return s
    if len(s) == 2:
        if s[0] != s[1]:
            return s[1]
        else:
            return s
    if s[0] == s[1]:
        s_max = (2, s[0:2])
    else:
        s_max = (1, s[0])
    for k in range(1, len(s) - 1):
        tmp_odd = oddHelper(s, k)
        tmp_even = evenHelper(s, k)
        if s_max[0] <= tmp_odd[0]:
            s_max = tmp_odd
        if s_max[0] <= tmp_even[0]:
            s_max = tmp_even
    return s_max[1]
