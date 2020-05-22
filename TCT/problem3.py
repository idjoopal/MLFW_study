# list를 두 subset list로 나누어 각 subset list의 합을 서로 뺀 값이 최소가 될 때, 그 값은?

# input 조건
# 2개 ~ 17개 정도의 숫자가 들어있는 list
# 각 원소는 음수 일 수 있다.
# 두 subset list에는 반드시 원소 하나 이상 들어가야 한다.


def solution(arr):

    sumTotal = sum(arr)
    subset1_sum = 0

    # 최초 주어진 리스트에 원소가 두개뿐이면 두개를 반드시 나눠주어야만 각 subset에 원소가 하나씩 포함될 수 있다.
    if len(arr) == 2:
        return abs(arr[0]-arr[1])
 
    return findMinRec(arr, len(arr), subset1_sum, sumTotal)

def findMinRec(arr,  length, subset1_sum, sumTotal): 
    # 다 확인하면 두 리스트 Sum의 차를 반환
    if length == 0 :
        return abs((sumTotal-subset1_sum) - subset1_sum)
        
    # 1번 subset에 넣을지, 2번 subset에 넣을지 선택.
    # 계속 선택하면서 넣다보면 나온 최솟값을 선택하게 될 것.
    return min(findMinRec(arr, length-1, subset1_sum+arr[length-1], sumTotal), findMinRec(arr, length-1, subset1_sum, sumTotal))