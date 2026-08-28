def solution(record):
    answer = []
    #[]님이 들어왔습니다/[]님이 나갔습니다.
    #닉네임 변경: 나갔다가 재입장/ 채팅방에서 닉네임 변경*소급 변경
    user = {}
    
    for update in record:
        msg = update.split(' ')
        if msg[0] == 'Leave':
            answer.append(f'{msg[1]}님이 나갔습니다.')
            continue
            
        uid, name = msg[1], msg[2]
        if msg[0] == 'Enter':
            user[uid] = name
            answer.append(f'{uid}님이 들어왔습니다.')
        else:
            user[uid] = name
    
    #마지막 저장 아이디로 변경하는게 빠를듯?
    for i in range(len(answer)):
        id = answer[i].split('님')[0]
        answer[i] = answer[i].replace(id,user[id])
        
    return answer