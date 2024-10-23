def min_attacks(T, test_cases):
    results = []
    for i in range(T):
        H, X, Y = test_cases[i]
        
        # Calculate the minimum number of attacks with and without the special attack
        attacks_with_special = (H - Y + X - 1) // X + 1
        attacks_without_special = (H + X - 1) // X
        
        # Choose the minimum of the two values
        results.append(min(attacks_with_special, attacks_without_special))
    
    return results

# Input reading
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Get results
results = min_attacks(T, test_cases)

# Output results
for result in results:
    print(result)