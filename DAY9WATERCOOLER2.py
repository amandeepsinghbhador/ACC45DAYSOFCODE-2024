# cook your dish here
T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())

    print((Y - 1) // X if X < Y else 0)