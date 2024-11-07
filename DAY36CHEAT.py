
T = int(input())

for _ in range(T):
    
    N = int(input())
    
    
    full_weeks = N // 7
    extra_days = N % 7
    
    
    tuesdays = full_weeks + (1 if extra_days >= 2 else 0)
    
    
    print(tuesdays)

