def cal_time(a, b):
    #a가 기준점 b가 변화량
    #a는 리스트형태로 들어옴
    
    #문자를 숫자로
    ts = int(a[0])*60 + int(a[1])
    ts += b #변화 반영
    
    return f'{str(ts//60).zfill(2)}:{str(ts%60).zfill(2)}' 


def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    for comm in commands:
        # 오프닝 건너뛰기 
        if op_start <=  pos <= op_end:
            #print('skip')
            pos = op_end
            
        if comm == 'prev':
            print('prev')
            pos = max('00:00', cal_time(pos.split(':'),-10))
            print(pos)
        else: #'next'
            #print('next')
            pos = min(video_len, cal_time(pos.split(':'),10))
            print(pos)
        
        # 오프닝 건너뛰기 
        if op_start <=  pos <= op_end:
            #print('skip')
            pos = op_end

    
    return pos