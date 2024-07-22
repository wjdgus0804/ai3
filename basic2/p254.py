def hello() :
    print('안녕하세요!')
for i in range(20) :
    hello()

# 1~100까지 합계 구하기
def uSum(uStart,uEnd) :
    sum=0
    for i in range(uStart,uEnd+1) :
        sum=sum+i
    print(sum)

def line() :
    print('-'*50)
# 만들어진 함수를 사용하는 쪽 - 비즈니스로직
# 합계가 3000이 넘는 순간 멈추기
# 합계, i값 출력하기
def sum_(n) :
    sum=0
    for i in range(1,101) :
        if sum>=n :
            break
        sum=sum+i
    print('%d 이상일 때 %d값  합계:%d'%(n,i,sum))


# 합계가 4000이 넘는 순간 멈추기
sum_(4000)

# 요구사항: 입력 2개 받기
# 시작수? 50
# 끝수? 200
# 50~200까지 합을 출력하기
start=int(input('시작수?'))
end=int(input('끝수?'))
uSum(start,end)

