def solution(arr):
    answer = [0, 0]
    N = len(arr)

    def check_quad(sx, ex, sy, ey):
        first = arr[sx][sy]

        # 전부 같은 값인지 확인
        same = True
        for i in range(sx, ex):
            for j in range(sy, ey):
                if arr[i][j] != first:
                    same = False
                    break
            if not same:
                break
        
        if same: #전부 같은 값이면
            answer[first] += 1
            return
        
        # 4분할
        mx = (sx + ex) // 2
        my = (sy + ey) // 2

        check_quad(sx, mx, sy, my)
        check_quad(mx, ex, sy, my)
        check_quad(sx, mx, my, ey)
        check_quad(mx, ex, my, ey)

    check_quad(0, N, 0, N)
    return answer