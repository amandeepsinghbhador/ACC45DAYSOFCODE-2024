# cook your dish here
T = int(input())

for _ in range(T):
    W, X, Y, Z = map(int, input().split())

    weights = [X, Y, Z]
    possible_weights = set()

    for i in range(1 << 3):
        weight = 0
        for j in range(3):
            if (i & (1 << j)) > 0:
                weight += weights[j]
        possible_weights.add(weight)

    if W in possible_weights:
        print("YES")
    else:
        print("NO")