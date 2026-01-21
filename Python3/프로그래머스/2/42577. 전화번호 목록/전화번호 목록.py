def solution(phone_book):
    # 전화번호부 형태로 배열해줘야함
    phone_book.sort()
    # 문자열 순으로 정렬되어 있다면 -> 따라서 바로 뒤에꺼랑만 비교
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    return True