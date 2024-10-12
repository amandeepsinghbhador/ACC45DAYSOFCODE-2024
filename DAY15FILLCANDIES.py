T = int(input())

for _ in range(T):
    N, K, M = map(int, input().split())

    total_capacity = K * M
    min_bags = (N + total_capacity - 1) // total_capacity
    print(min_bags)
