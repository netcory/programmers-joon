def solution(name, yearning, photo):
    answer = []
    name_yearning_dict = {}

    for i in range(len(name)):
        name_key = name[i]
        yearning_value = yearning[i]
        name_yearning_dict[name_key] = yearning_value

    for one_photo in photo:
        score = 0
        
        for one_name in one_photo:
            if one_name in name_yearning_dict:
                score += name_yearning_dict[one_name]
        
        answer.append(score)

    return answer