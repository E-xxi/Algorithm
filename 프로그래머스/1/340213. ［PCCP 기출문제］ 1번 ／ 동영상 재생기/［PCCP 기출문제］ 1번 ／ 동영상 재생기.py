def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    def time_lim(t, change):
        #양쪽 시간 처리
        em, es = map(int,video_len.split(':'))
        end_time = em*60 + es
    
        if t + change < 10:
            return 0
        elif end_time - (t + change) < 10:
            return end_time
        
        return t + change
    
        
    m, s = map(int,pos.split(':'))
    time = m*60 + s
    
    opsm, opss = map(int,op_start.split(':'))
    ops = opsm*60 + opss
    
    opem, opes = map(int,op_end.split(':'))
    ope = opem*60 + opes
    

            
    for command in commands:
        #print(f'{time//60:02d}:{time%60:02d}')
        
        if ops <= time <= ope:
            time = ope
        if command == 'prev':
            time = time_lim(time, -10)
        elif command == 'next':
            time = time_lim(time, 10)
        
    if ops <= time <= ope:
        time = ope
        
        
    
    return f'{time//60:02d}:{time%60:02d}'