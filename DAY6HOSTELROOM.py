T = int(input())

for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    max_people = X
    current_people = X

    for i in range(N):
        current_people += A[i]
        max_people = max(max_people, current_people)

    print(max_people)