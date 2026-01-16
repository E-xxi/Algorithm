def solution(id_list, report, k):
    #동일한 유저 신고 횟수는 1회로
    #k번 신고시 메일, 신고자들에게 메일 감. < 신고자들 카운트.
    answer = {id: 0 for id in id_list}
    report = set(report) #신고자, 신고당한자가 같으면 어차피 1회 카운트
    
    mail = {id: [] for id in id_list}
    for r in report:
        mail[r.split()[1]].append(r.split()[0]) #신고자들 더하기 
    
    for w in mail:
        if len(mail[w]) >= k:
            for m in mail[w]:
                answer[m] += 1
            
    return list(answer.values())