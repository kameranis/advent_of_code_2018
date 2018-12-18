s = [ord(c) for c in input()]
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
s = ''.join([chr(c) for c in s])
print(s)
print(len(s))
