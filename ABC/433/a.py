X, Y, Z = map(int,input().split())

X_MAX = 100
RESULT_MESSAGE = "No"

for i in range(X_MAX):
    if X == Y * Z:
        RESULT_MESSAGE = "Yes"
        break
    X+=1
    Y+=1

print(RESULT_MESSAGE)
