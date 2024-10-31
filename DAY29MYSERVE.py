
T = int(input())

results = []
for _ in range(T):
 
    P, Q = map(int, input().split())
    
    
    total_points = P + Q

    group = total_points // 2
    if group % 2 == 0:
        results.append("Alice")
    else:
        results.append("Bob")

for result in results:
    print(result)
