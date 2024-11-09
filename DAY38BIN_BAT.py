import math


T = int(input())

for _ in range(T):

    N, A, B = map(int, input().split())
    

    rounds = int(math.log2(N))
    
    
    total_time = (rounds * A) + ((rounds - 1) * B)
    
    print(total_time)
