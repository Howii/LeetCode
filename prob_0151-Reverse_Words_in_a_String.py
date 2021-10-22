def reverseWords1(s: str) -> str:
    word_list = []
    buffer = []
    for c in s:
        if c != ' ':
            buffer.append(c)
        elif buffer:
            word = ''.join(buffer)
            word_list.append(word)
            buffer = []
    if buffer:
        word = ''.join(buffer)
        word_list.append(word)
    
    return " ".join(reversed(word_list))

def reverseWords2(s: str) -> str:
    return " ".join(reversed(s.split()))
