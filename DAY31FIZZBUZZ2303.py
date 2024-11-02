
T = int(input())


results = []
for _ in range(T):
    N = int(input())
    
    choices = N * (N - 1)
    results.append(choices)


for result in results:
    print(result)
