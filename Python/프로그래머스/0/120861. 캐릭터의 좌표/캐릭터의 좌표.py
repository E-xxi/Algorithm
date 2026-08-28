def solution(keyinput, board):
    answer = [0,0]
    dxy = {'up': (0,1), 'down': (0,-1), 'left': (-1,0), 'right':(1,0)}
    
    for key in keyinput:
        #print(answer)
        dx, dy = dxy[key]
        nx, ny = answer[0]+dx, answer[1]+dy
        
        if -board[0]//2<nx<= board[0]//2 and -board[1]//2<ny<= board[1]//2:
            answer = [nx,ny]
            
    return answer