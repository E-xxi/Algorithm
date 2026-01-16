def solution(genres, plays):
    answer = []
    #장르별로 가장 많이 재생된 노래를 최대 두개 모아 베스트앨범 출시.  
    genre_l = {} #{'classic': {0: 500,}, 'pop': {1: 600, 4: 2500}} 이런 딕셔너리 
    for idx, z in enumerate(zip(genres, plays)):
        if z[0] not in genre_l.keys():
            genre_l[z[0]] = {}
        genre_l[z[0]][idx] = z[1] 
    
    #장르의 value값을 sum해서 내림차순 정렬
    genre_l = dict(sorted(genre_l.items(), key = lambda x:sum(x[1].values()), reverse = True))
    #print(genre_l)
    
    #각 장르별 딕셔너리를 정렬해서 추출
    for g in genre_l.keys():
        songs_l = list(dict(sorted(genre_l[g].items(), key = lambda x:x[1], reverse = True)).keys())
        #print(songs_l)
        #상위 2개 리턴
        answer += songs_l[:min(len(songs_l),2)]
    
    return answer