
T = int(input())

for _ in range(T):
  
    N = int(input())
    A = list(map(int, input().split()))
    
    
    S = sum(A)
    
    
    if S == 0:
        print(0)
        continue
    
    
    if abs(S) % 2 != 0:
        print(-1)
        continue
    
    
    flips_needed = abs(S) // 2
    print(flips_needed)
