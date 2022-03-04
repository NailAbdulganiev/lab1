s = input()
counter = 1
i = 0
while (i + 1 != len(s)):
    if (s[i] == s[i + 1]):
        counter += 1
    else:
        print(str(counter) + ' ' + s[i])
        counter = 1
    i += 1
print(str(counter) + ' ' + s[i])