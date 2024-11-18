def is_jenga_valid(T, test_cases):
    results = []
    for N, X in test_cases:
        # Check if X is divisible by N
        if X % N == 0:
            results.append("YES")
        else:
            results.append("NO")
    return results

# Input reading
T = int(input())  # Number of test cases
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Processing and output
results = is_jenga_valid(T, test_cases)
print("\n".join(results))
