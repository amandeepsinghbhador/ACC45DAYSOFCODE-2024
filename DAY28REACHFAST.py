
T = int(input())


results = []
for _ in range(T):
    
    A, B, K = map(int, input().split())
    
    
    distance = abs(B - A)
    
    steps = (distance + K - 1) // K
    
    
    results.append(steps)


for result in results:
    print(result)
