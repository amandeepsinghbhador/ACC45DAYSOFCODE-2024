
T = int(input())


for _ in range(T):
    
    X, Y = map(int, input().split())
    
    
    if Y >= X / 2:
        print("YES")
    else:
        print("NO")

