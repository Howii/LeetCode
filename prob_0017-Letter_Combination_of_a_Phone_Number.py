from itertools import product

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    digit2str = {"2" : "abc", "3" : "edf", "4" : "ghi", "5" : "jkl",
                 "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
    bar = [digit2str[d] for d in digits]
    return ["".join(x) for x in product(*bar)] if bar else []
