def divide(self, dividend: int, divisor: int) -> int:
    if (dividend >= 0 and divisor > 0) or (dividend < 0 and divisor < 0):
        negative = False
    else:
        negative = True
    dividend, divisor = abs(dividend), abs(divisor)

    tmpA = 1
    tmpB = divisor
    powerA = [tmpA] 
    powerB = [tmpB]    
    for i in range(31):
        tmpA = tmpA + tmpA
        tmpB = tmpB + tmpB
        powerA.append(tmpA)
        powerB.append(tmpB)

    powerA.reverse()
    powerB.reverse()

    if negative:
        if dividend > tmpB:
            return tmpB - 1
        elif dividend == tmpB:
            return -tmpB
    elif dividend >= tmpB - 1:
        return tmpB - 1

    out = 0
    for a, b in zip(powerA, powerB):
        if dividend >= b:
            out += a
            dividend -= b

    if negative:
        return -out
    else:
        return out
