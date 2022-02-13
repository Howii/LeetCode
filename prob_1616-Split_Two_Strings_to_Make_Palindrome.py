def checkPalindrome(s: str) -> bool:
    N = len(s)
    for i in range(N // 2):
        if s[i] != s[N - i - 1]:
            return False
    return True

def checkPalindromeFormation(a: str, b: str) -> bool:
    # assume a and b have the same length
    # if either a or b is palindrome, then true
    if checkPalindrome(a) or checkPalindrome(b):
        return True

    N = len(a)
    # check a_prefix + b_suffix
    i = 0
    while i < N - i - 1:
        if a[i] == b[N - i - 1]:
            i += 1
        else:
            break
    if checkPalindrome(a[i:(N-i)]):
        output = a[:(N-i)] + b[(N-i):]
        print(output)
        return True
    if checkPalindrome(b[i:(N-i)]):
        output = a[:i] + b[i:]
        print(output)
        return True

    # check b_prefix + a_suffix
    i = 0
    while i < N - i - 1:
        if b[i] == a[N - i - 1]:
            i += 1
        else:
            break
    if checkPalindrome(b[i:(N-i)]):
        output = b[:(N-i)] + a[(N-i):]
        print(output)
        return True
    if checkPalindrome(a[i:(N-i)]):
        output = b[:i] + a[i:]
        print(output)
        return True

    return False

### TEST
b = 'ulatcfd'
a = 'jiztalu'
print(a)
print(b)
print('-----------')
if checkPalindromeFormation(a, b):
    print("Formation found")

