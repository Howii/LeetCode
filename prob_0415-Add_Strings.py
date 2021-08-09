def addStrings(num1: str, num2: str) -> str:
    out_list = []
    num1_list = list(num1)
    num2_list = list(num2)
    plus = 0
    while num1_list or num2_list:
        x = int(num1_list.pop()) if num1_list else 0
        y = int(num2_list.pop()) if num2_list else 0
        z = x + y + plus
        if z < 10:
            out_list.append(str(z))
            plus = 0
        else:
            out_list.append(str(z)[1])
            plus = 1
    
    if plus:
        out_list.append("1")
    
    out_list.reverse()
    out = "".join(out_list)
    return out

## Test
num1 = "987654"
num2 = "23456"
print(addStrings(num1, num2))
