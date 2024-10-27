
T = int(input())

# Processing each test case
results = []
for _ in range(T):
    # Reading tastiness values for ingredients A, B, C, D
    a, b, c, d = map(int, input().split())
    
    # Calculate the maximum tastiness by checking all combinations
    max_tastiness = max(a + c, a + d, b + c, b + d)
    
    # Store the result for each test case
    results.append(max_tastiness)

# Output all results
for result in results:
    print(result)
