
T = int(input())


for _ in range(T):
    N, X, P = map(int, input().split())
    
    total_score = 4 * X - N
    
    if total_score >= P:
        print("PASS")
    else:
        print("FAIL")
