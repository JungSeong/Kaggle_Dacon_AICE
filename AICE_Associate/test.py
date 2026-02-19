import sys
input = sys.stdin.readline

n = int(input())
l = []

for _ in range(n) :
    name, dd, mm, yyyy = input().split()
    dd, mm, yyyy = int(dd), int(mm), int(yyyy)
    l.append([name, dd, mm, yyyy])

l.sort(key=lambda x : (x[3], x[2], x[1]))

print(l[-1][0])
if n >= 1 :
    print(l[0][0])