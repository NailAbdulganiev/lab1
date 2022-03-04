a = map(int, input().split())
print(*[i * i for i in a if i % 2 != 0 and i != 3 and i != 7])