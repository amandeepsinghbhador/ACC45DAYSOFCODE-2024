T = int(input())

for _ in range(T):
    dragon_scores = list(map(int, input().split()))
    sloth_scores = list(map(int, input().split()))

    dragon_total = sum(dragon_scores)
    sloth_total = sum(sloth_scores)

    if dragon_total > sloth_total:
        print("Dragon")
    elif dragon_total < sloth_total:
        print("Sloth")
    else:
        if dragon_scores[0] > sloth_scores[0]:
            print("Dragon")
        elif dragon_scores[0] < sloth_scores[0]:
            print("Sloth")
        else:
            if dragon_scores[1] > sloth_scores[1]:
                print("Dragon")
            elif dragon_scores[1] < sloth_scores[1]:
                print("Sloth")
            else:
                print("Tie")
