def check_input(element=None):
    return isinstance(element, str)


def get_substring(s=""):
    if not isinstance(s, str) or not s:
        return ""

    last_pos = {}
    left = 0
    best_len = 0
    best_start = 0

    for right, ch in enumerate(s):
        if ch in last_pos and last_pos[ch] >= left:
            left = last_pos[ch] + 1

        last_pos[ch] = right
        curr_len = right - left + 1

        if curr_len > best_len:
            best_len = curr_len
            best_start = left

    return s[best_start:best_start + best_len]


def main(arr=None):
    if arr is None:
        arr = []

    max_idx = -1
    max_len = -1
    max_str = ""

    for i, el in enumerate(arr):
        if check_input(el) and len(el) > max_len:
            max_len = len(el)
            max_idx = i
            max_str = el

    substr = "" if max_idx == -1 else get_substring(max_str)
    print(f"{max_idx}; {substr!r}")
    return max_idx, substr
