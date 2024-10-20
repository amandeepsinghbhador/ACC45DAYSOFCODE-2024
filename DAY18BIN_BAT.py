import math

def total_event_time(T, test_cases):
    results = []
    for i in range(T):
        N, A, B = test_cases[i]
        
        # Calculate the number of rounds
        R = int(math.log2(N))
        
        # Calculate total time
        total_time = R * A + (R - 1) * B
        results.append(total_time)
    
    return results

# Input reading
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Get results
results = total_event_time(T, test_cases)

# Output results
for result in results:
    print(result)
