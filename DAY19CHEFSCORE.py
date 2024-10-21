def can_achieve_score(T, test_cases):
    results = []
    for i in range(T):
        N, X, Y = test_cases[i]
        
        # Check if Y is a multiple of X and does not exceed N*X
        if Y % X == 0 and Y <= N * X:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Input reading
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Get results
results = can_achieve_score(T, test_cases)

# Output results
for result in results:
    print(result)