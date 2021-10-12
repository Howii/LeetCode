def reorderSpaces(text: str) -> str:
    spaces = 0
    words = []
    tmp = []
    for c in text:
        if c != ' ':
            tmp.append(c)
        else:
            spaces += 1
            if tmp:
                word = ''.join(tmp)
                words.append(word)
                tmp = []
    if tmp:
        word = ''.join(tmp)
        words.append(word)

    num_gaps = len(words) - 1
    if num_gaps == 0:
        gap_size = 0
        trailing = spaces
    else:
        gap_size = spaces // num_gaps
        trailing = spaces % num_gaps
    
    out = (' ' * gap_size).join(words) + (' ' * trailing)
    return out

## Test Case
txt = " practice   makes   perfect"
print("\'" + reorderSpaces(txt) + "\'")
