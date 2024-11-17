import math

def calculate_max_plates(T, test_cases):
    results = []
    for case in test_cases:
        X, Y, R = case
        extra_sticks = R // 30  # Calculate extra sticks
        total_sticks = X + extra_sticks  # Total sticks eaten
        max_plates = math.ceil(total_sticks / Y)  
        results.append(max_plates)
    return results

# Input reading
T = int(input())  # Number of test cases
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Processing and output
results = calculate_max_plates(T, test_cases)
print("\n".join(map(str, results)))
