
N = int(input())


cumulative_score1 = 0
cumulative_score2 = 0
max_lead = 0
winner = 0


for _ in range(N):
    
    S, T = map(int, input().split())
    
    # Update cumulative scores
    cumulative_score1 += S
    cumulative_score2 += T
    
    # Calculate the lead and determine the leader for this round
    if cumulative_score1 > cumulative_score2:
        lead = cumulative_score1 - cumulative_score2
        leader = 1
    else:
        lead = cumulative_score2 - cumulative_score1
        leader = 2
    
    # Update max lead and winner if current lead is the largest so far
    if lead > max_lead:
        max_lead = lead
        winner = leader

# Output the winner and the maximum lead
print(winner, max_lead)
