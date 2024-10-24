def find_polynomial_degree(T, test_cases):
    results = []
    for i in range(T):
        N = test_cases[i][0]
        coefficients = test_cases[i][1]
        
        # Find the degree by checking coefficients from the end
        degree = -1
        for j in range(N - 1, -1, -1):
            if coefficients[j] != 0:
                degree = j
                break
        
        results.append(degree)
    
    return results

# Input reading
T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    coefficients = list(map(int, input().split()))
    test_cases.append((N, coefficients))

# Get results
results = find_polynomial_degree(T, test_cases)

# Output results
for result in results:
    print(result)