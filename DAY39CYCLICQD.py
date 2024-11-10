
T = int(input())

results = []
for _ in range(T):
    # Read angles A, B, C, D
    A, B, C, D = map(int, input().split())
    
    # Check if opposite pairs sum to 180
    if A + C == 180 and B + D == 180:
        results.append("YES")
    else:
        results.append("NO")

# Output all results
print("\n".join(results))
