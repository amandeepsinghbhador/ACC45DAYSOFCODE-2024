
T = int(input())


for _ in range(T):
    X, Y = map(int, input().split())
   
    max_people = (X // Y) // 2
    print(max_people)
