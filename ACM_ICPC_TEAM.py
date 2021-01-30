def acmTeam(topic):
    no_of_team = 0
    max_score = 0
    for i in range(len(topic)-1):
        for j in range(i+1,len(topic)):
            temp_score = bin((int(topic[i],2))|(int(topic[j],2))).count('1')
            if temp_score>max_score:
                max_score=temp_score
                no_of_team=1
            elif temp_score == max_score:
                no_of_team+=1
    return [max_score,no_of_team]
