def solution(message, spoiler_ranges):
    msg = message.split()
    message = list(message)

    # 추가:
    # 각 문자 인덱스가 몇 번째 단어에 속하는지 저장
    # 공백은 단어가 아니므로 -1
    word_idx = [-1] * len(message)

    idx = 0
    for i in range(len(message)):
        if message[i] != ' ':
            word_idx[i] = idx

            # 현재 문자가 단어의 마지막 문자면 다음 단어로 넘어감
            if i + 1 == len(message) or message[i + 1] == ' ':
                idx += 1

    # 추가:
    # 각 단어에 아직 안 열린 스포 문자가 몇 개 남았는지 저장
    hidden_cnt = [0] * len(msg)

    # 추가:
    # 스포 방지 단어인지 여부 저장
    is_secret_word = [False] * len(msg)

    # 기존 흐름 유지:
    # 처음에는 스포 구간 문자를 '-'로 바꿈
    for start, end in spoiler_ranges:
        for i in range(start, end + 1):
            if message[i] != ' ':
                w = word_idx[i]
                message[i] = '-'
                hidden_cnt[w] += 1
                is_secret_word[w] = True

    blur = ''.join(message).split(' ')

    # 수정:
    # 기존에는 여기서 '-'가 포함된 단어를 바로 secret에 넣었음.
    # 하지만 단어가 여러 스포 구간에 걸쳐 있으면,
    # 아직 완전히 공개되지 않았을 수 있으므로 여기서 세면 안 됨.
    #
    # 대신 blur에는 "일반 구간에 보이는 단어"만 남기기 위해
    # 스포 방지 단어 자리는 '-'로 바꿔둠.
    for idx, word in enumerate(blur):
        if '-' in word:
            blur[idx] = '-'

    normal_words = set(blur)

    secret = set()
    answer = 0

    # 추가:
    # 스포 구간을 왼쪽 -> 오른쪽 순서로 클릭하면서 확인
    for start, end in spoiler_ranges:
        opened = []

        for i in range(start, end + 1):
            if word_idx[i] == -1:
                continue

            w = word_idx[i]

            # 이 문자가 열렸으므로 해당 단어의 숨겨진 문자 수를 줄임
            hidden_cnt[w] -= 1

            # hidden_cnt[w]가 0이면
            # 이 단어의 모든 스포 문자가 지금 막 공개된 것
            if hidden_cnt[w] == 0:
                opened.append(w)

        # 같은 구간 안에서 한 단어의 여러 글자가 열릴 수 있으므로 중복 제거
        # 동시에 여러 단어가 공개되면 왼쪽부터 판단해야 하므로 정렬
        opened = sorted(set(opened))

        for w in opened:
            word = msg[w]

            # 중요 단어 조건:
            # 1. 스포 방지 단어이고
            # 2. 일반 구간에 등장하지 않았고
            # 3. 이전에 공개된 스포 단어가 아니어야 함
            if word not in normal_words and word not in secret:
                answer += 1

            # 중요 단어가 아니어도
            # "이미 공개된 스포 방지 단어"에는 포함해야 함
            secret.add(word)

    return answer