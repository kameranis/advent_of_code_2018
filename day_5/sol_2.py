a = ord('a')
A = ord('A')

original_s = [ord(c) for c in input()]

best_len = len(original_s)
for offset in range(26):
    s = [c for c in original_s if (c - a - offset != 0) and (c - A - offset != 0)]

    guard = True
    diff = abs(ord('A') - ord('a'))
    while guard:
        guard = False
        new_s = []
        i = 1
        while i < len(s):
            if abs(s[i] - s[i-1]) == diff:
                guard = True
                i += 2
            else:
                new_s.append(s[i-1])
                i += 1
        if i == len(s):
            new_s.append(s[-1])
        s = new_s
    print(chr(A + offset), len(s))
    if len(s) < best_len:
        best_len = len(s)
print(best_len)
