
T = int(input())
results = []
for _ in range(T):
    # Read N and K values
    N, K = map(int, input().split())
    # Read the list of characteristic values
    characteristics = list(map(int, input().split()))
    
    # Count Wolverine-like minions
    wolverine_count = sum(1 for characteristic in characteristics if (characteristic + K) % 7 == 0)
    
    # Store the result for this test case
    results.append(wolverine_count)

# Print all results for each test case
for result in results:
    print(result)
