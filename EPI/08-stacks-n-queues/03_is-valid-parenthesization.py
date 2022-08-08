def is_well_formed(s: str) -> bool:
    left_chars, lookup = [], {"(": ")", "{": "}", "[": "]"}
    for c in s:
        if c in lookup:  # opener
            left_chars.append(c)
        elif not left_chars or lookup[left_chars.pop()] != c:  # closer
            # Unmatched right char or mistmatched chars.
            return False
    return not left_chars
