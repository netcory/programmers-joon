def solution(number, limit, power):
    answer = 0
    
    divisor_cnt_list = []
    divisor_cnt = 0
    for i in range(1, number + 1):
        divisor_list = []
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                divisor_list.extend([j, i // j])
        divisor_cnt_list.append(len(set(divisor_list)))
     
    for divisor_cnt in divisor_cnt_list:
        if divisor_cnt > limit:
            answer += power
        else:
            answer += divisor_cnt

    return answer