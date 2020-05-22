def solution(rows, columns, swipes):
    answer = []
    # 전체 list 만들기
    maps = []
    for r in range(0, rows):
        rowList = []
        for c in range(0, columns):
            rowList.append(columns * r + c + 1)
        maps.append(rowList)
    
    print(maps)
    # swipe하기
    for swipe in swipes:
        d, r1, c1, r2, c2 = swipe
        
        # swipe할 일부를 추출
        sub_maps = []
        for r in range(r1-1, r2):
            rowList = []
            for c in range(c1-1, c2):
                rowList.append(maps[r][c])
            sub_maps.append(rowList)
        
        print(sub_maps)
        # 추출한 부분 list를 swipe
        swiped_arr, moved_sum = swiping(r2-r1, c2-c1, sub_maps, d)
        # 옮김당한 줄의 합을 정답에 추가
        print(swiped_arr)
        answer.append(moved_sum)

        # swipe한 일부를 다시 전체에 삽입
        for r in range(r1-1, r2):
            for c in range(c1-1, c2):
                maps[r][c] = swiped_arr[r-(r1-1)][c-(c1-1)]
        
        print(maps)
                
    return answer

def swiping(row_len, col_len, arr, d):
    if d==1:
        # UP - 맨 윗줄이 밑으로 붙음
        moved_sum = sum(arr[0])
        arr.append(arr[0])
        arr.pop(0)
    elif d==2:
        # DOWN - 맨 아랫줄이 위로 붙음
        moved_sum = sum(arr[row_len-1])
        arr.insert(0, arr[row_len-1])
        arr.pop()
    elif d==3:
        # LEFT - 맨 왼쪽줄이 오른쪽으로 붙음
        moved_arr = []
        for r in range(0, row_len+1):
            moved_arr.append(arr[r][0])
            arr[r].append(arr[r][0])
            arr[r].pop(0)
        moved_sum = sum(moved_arr)
    elif d==4:
        # RIGHT - 맨 오른쪽줄이 왼쪽으로 붙음
        moved_arr = []
        for r in range(0, row_len+1):
            moved_arr.append(arr[r][col_len])
            arr[r].insert(0, arr[r][col_len])
            arr[r].pop()
        moved_sum = sum(moved_arr)

    return arr, moved_sum