def solution(code):
    mode = False
    ret = []
    
    for idx in range(len(code)):
        if mode == False:   
            if (code[idx] != '1') and (idx % 2 == 0):
                    ret.append(code[idx])               
        else:
            if (code[idx] != '1') and (idx % 2 == 1):
                    ret.append(code[idx])   
        if code[idx] == '1':
            mode = not mode
        
    if len(ret) == 0:
        return 'EMPTY'
    return ''.join(ret)