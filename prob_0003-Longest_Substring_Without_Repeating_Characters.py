def lengthOfLongestSubstring(s: str) -> int:
    if len(s) < 2:
        return len(s)
    i = j = 0
    current_string = s[0]
    current_length = max_length = 1
    while j < len(s) - 1:
        if s[j+1] not in current_string:
            current_string += s[j+1]
            current_length += 1
            j += 1
            if current_length > max_length:
                max_length = current_length
        else:
            j += 1
            while s[i] != s[j]:
                i += 1
            if i < j:
                i += 1
            current_string = s[i:(j + 1)]
            current_length = j - i + 1
    return max_length
