data = [int(i) for i in input().split()]

i = 0
result = 0

def count():
    children = data[i]
    global i, result
    i += 1
    data_entries = data[i]
    i += 1
    for child in range(children):
        count()
    for _ in range(data_entries):
        result += data[i]
        i += 1
    return

count()
print(result)
