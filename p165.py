# while문
# while 조건식:
#     참이면 수행하는 문장
# 조건식 거짓이면 처리
# 도는 조건식 다음으로 처리

'''
sum=0
i=1
while i<=10 :
    sum=sum+i
    i=i+1
print('합계는 %d'%sum)

# 500~600까지의 정수 중 5의 배수 합계를 구하는 프로그램
i=500
sum=0
while i<=600 :
    if i%5==0 :
        sum=sum+i
    i=i+1
print('합계는:%d'%sum)

# 1~1000까지 정수 중 100의 배수를 제외하고 합계를 구하기
i=1
sum=0
while i<=1000 :
    if i%100!=0 :
        sum=sum+i
    i=i+1
print('합계는:%d'%sum)

s='Python is widely used by a number of big companies'

i=0
count=0
print('모음:',end=' ')
while i<=len(s)-1 :
    if (s[i]=='a' or s[i]=='A' or s[i]=='e' or s[i]=='E' or s[i]=='i' or s[i]=='I' or s[i]=='o' or s[i]=='O' or s[i]=='u' or s[i]=='U') :
        count=count+1
        print(s[i],end=' ')
    i=i+1
print()
print('모음 개수:%d'%count)

i=0
count=0
print('자음:',end=' ')
while i<=len(s)-1 :
    if (s[i]!=' ' and not(s[i]=='a' or s[i]=='A' or s[i]=='e' or s[i]=='E' or s[i]=='i' or s[i]=='I' or s[i]=='o' or s[i]=='O' or s[i]=='u' or s[i]=='U')):
        count=count+1
        print(s[i],end=' ')
    i=i+1
print()
print('자음 개수:%d'%count)


# 숫자 2개를 입력 받아서 덧셈하기
yN='y'
while yN=='y' :
    num1=int(input('첫 번째 숫자를 입력하세요:'))
    num2=int(input('두 번째 숫자를 입력하세요:'))
    sum=num1+num2
    print('합계:%d'%sum)
    yN=input('계속 하시겠습니까?(y:계속, n:그만):')


while True:
    w=input('문자1:')
    s=input('문자2:')
    ws=''
    for i in range(len(w)+len(s)) :
        if i <= len(w)-1 :
            ws=ws+w[i]
        if i <= len(s)-1 :
            ws=ws+s[i]
    print(ws)
    yN=input('계속 하실래요?(y/n)')
    if yN=='n' :
        break
'''

