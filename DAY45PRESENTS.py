
T = int(input())


for _ in range(T):
    N = int(input())
    
    full_groups = N // 5
    remaining = N % 5
    
    total_coins = (full_groups * 4) + remaining
    
    print(total_coins)
