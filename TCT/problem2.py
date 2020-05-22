# 0과 1로 이루어진 문자열을 연속하는 차례대로 자른뒤
# 각 잘라낸 문자열을 2진법으로 변환하여 다시 붙인다.
# 해당 작업을 k번 반복하면 나오는 문자열은?

def solution(numstr, k):
    answer = '' 

    for i in range(0, k):
        sub_now = ''
        for n in range(0, len(numstr)-1):
            if numstr[n] != numstr[n+1]:
                sub_now += numstr[n]
                answer += ch_bin(int(sub_now))
                sub_now = ''
            else:
                sub_now += numstr[n]
                continue
        sub_now += numstr[len(numstr)-1]
        answer += ch_bin(int(sub_now))
        numstr = answer
        answer = ''

    return numstr


def ch_bin(my_int):
    print(my_int, 'changed to',"{0:#b}".format(my_int).split('b')[1])
    return "{0:#b}".format(my_int).split('b')[1]