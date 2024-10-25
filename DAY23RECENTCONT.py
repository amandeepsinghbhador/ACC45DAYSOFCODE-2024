def count_problems(T, test_cases):
    results = []
    for i in range(T):
        N = test_cases[i][0]
        contest_codes = test_cases[i][1]
        
        count_start38 = 0
        count_ltime108 = 0
        
        for code in contest_codes:
            if code == "START38":
                count_start38 += 1
            elif code == "LTIME108":
                count_ltime108 += 1
        
        results.append((count_start38, count_ltime108))
    
    return results

# Input reading
T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    contest_codes = input().split()
    test_cases.append((N, contest_codes))

# Get results
results = count_problems(T, test_cases)

# Output results
for result in results:
    print(result[0], result[1])