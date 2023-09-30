letters = input()

result = ''
ints = 0
strs = []

# int, str 구별해서 담기 + 더하기 하면 될거 같은데!
for l in letters:
    try:
        if type(int(l)) == int:
            ints += int(l)
    except:
        strs.append((l, ord(l)))


strs.sort(key=lambda x: x[1])
print(strs)

result = ''
for s in strs:
    result += s[0]

print(result + str(ints))
