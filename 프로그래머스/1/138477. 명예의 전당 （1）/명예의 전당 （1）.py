def solution(k, score):
    answer = []
    hall_of_fame = []

    total_days = len(score)

    for i in range(0, total_days):
        if i <= k - 1:
            answer.append(min(score[:i + 1]))
            hall_of_fame.append(score[i])
        else:
            hall_of_fame.append(score[i])
            minimum = min(hall_of_fame)
            hall_of_fame.remove(minimum)
            answer.append(min(hall_of_fame))
                        
    return answer