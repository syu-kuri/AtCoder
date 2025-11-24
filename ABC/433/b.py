N = int(input())
A = list(map(int, input().split()))

ans = []

for i in range(N):
    idx = -1
    for j in range(i - 1, -1, -1):
        if A[j] > A[i]:
            idx = j + 1
            break
    ans.append(idx)

print(*ans)
