
T = int(input())


for _ in range(T):
    A, B, C = map(int, input().split())
    
    total_cost = A + B + C - min(A, B, C)
    print(total_cost)
