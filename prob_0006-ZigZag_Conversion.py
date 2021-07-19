def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1 or numRows >= len(s):
        return s
    table = [""] * numRows
    i = 0
    for letter in s:
        if i == 0:
            step = 1
        elif i == numRows - 1:
            step = -1
        table[i] += letter
        i += step
    return "".join(table)
