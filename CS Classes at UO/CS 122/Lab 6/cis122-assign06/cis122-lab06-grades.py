input_grades = True
counter = 0
total_sum = 0
lowest_score = 99999999
highest_score = -99999999

while input_grades:
    score = input("Enter score: ")
    if len(score) == 0:
        input_grades = False
    else:
        score = int(score)
        if 0 <= score <= 100:
            total_sum += score
            counter += 1
            if score < lowest_score:
                lowest_score = score
            if score > highest_score:
                highest_score = score
        else:
            print("Score must be between 0 and 100")

if counter > 0:
    print("***Results***")
    print("Count: " , counter)
    print("Average: " , round(total_sum/counter, 2))
    print("Low score: " , lowest_score)
    print("High score: " , highest_score)
else:
    print("No scores entered")
