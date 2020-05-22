# 1번
# 주어진 a,b,c 중 두개를 선택해서 더하거나 빼거나 곱하여 나올 수 있는 모든 조합 중 가장 큰 것은?
# a,b,c는 음수도 포함된다.

def solution(a,b,c):
    answer = -1

    answer = max( answer, a+b )
    answer = max( answer, b+c )
    answer = max( answer, a+c )

    answer = max( answer, a-b )
    answer = max( answer, b-c )
    answer = max( answer, a-c )
    answer = max( answer, b-a )
    answer = max( answer, c-b )
    answer = max( answer, c-a )
    
    answer = max( answer, a*b )
    answer = max( answer, b*c )
    answer = max( answer, a*c )

    return answer