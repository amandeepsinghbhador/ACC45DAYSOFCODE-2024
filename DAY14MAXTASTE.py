T = int(input())

for _ in range(T):
    a, b, c, d = map(int, input().split())

    max_tastiness = max(a + c, a + d, b + c, b + d)
    print(max_tastiness)
