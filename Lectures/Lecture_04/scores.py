scores = []
try:
    score = int(input("score: "))
except ValueError:
    print("invalid Score")

while score >= 0:
    scores.append(score)
    score = int(input("Score: "))
print("Your Highest score is", max(scores))
