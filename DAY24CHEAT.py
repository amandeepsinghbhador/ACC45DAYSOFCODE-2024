
T = int(input())
results = []
for _ in range(T):
    N = int(input())
    
    # Calculate full weeks and the remaining days
    full_weeks = N // 7
    remaining_days = N % 7
    
    # Calculate the total number of Tuesdays
    tuesdays_count = full_weeks
    if remaining_days >= 2:  # if remaining days include Tuesday
        tuesdays_count += 1
    
    # Store result for each test case
    results.append(tuesdays_count)

# Output all results
for result in results:
    print(result)
