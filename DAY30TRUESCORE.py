
T = int(input())
results = []
for _ in range(T):
    
    A, B = map(int, input().split())
    
    C, D = map(int, input().split())
    
    
    if C >= A and D >= B:
        results.append("POSSIBLE")
    else:
        results.append("IMPOSSIBLE")
for result in results:
    print(result)
