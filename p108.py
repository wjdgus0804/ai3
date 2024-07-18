# 배수
# num=int(input('양의 정수를 입력하세요:'))
# result='3의 배수도 4의 배수도 아니다.'
# if num%3==0 :
#     result='3의 배수이다.'
# if num%4==0 :
#     result='4의 배수이다.'
# if num%3==0 and num%4==0 :
#     result='3의 배수이면서 4의 배수이다.'

# print('%d는 %s'%(num,result))


# num1=int(input('양의 정수를 입력하세요:'))
# result1=num1
# if num1%2==0 and num1%4==0 :
#     result1='행운의 수'
# print(result1)


# ans1=input("'사자'의 영어 단어는 무엇일까요?:")
# result='땡! 틀렸습니다.'
# if ans1=='lion' :
#     result='딩동댕! 참 잘했어요~'
# print(result)

# ans2=input("'오렌지'의 영어 단어는 무엇일까요?:")
# result1='땡! 틀렸습니다.'
# if ans2=='orange' :
#     result1='딩동댕! 참 잘했어요~'
# print(result1)

# ans3=input("'기차'의 영어 단어는 무엇일까요?:")
# result2='땡! 틀렸습니다.'
# if ans3=='train' :
#     result2='딩동댕! 참 잘했어요~'
# print(result2)


# start=int(input('시작 수는?:'))
# end=int(input('끝 수는?:'))
# num=int(input('정수를 입력하세요:'))
# result='%d는 %d~%d 사이에 없다.'%(num,start,end)
# if num>start and num<end :
#     result='%d는 %d~%d 사이에 있다.'%(num,start,end)
# print(result)

        
# month=int(input('월을 숫자로 입력하세요.:'))
# if month=='3' or month=='4' or month=='5' :
#     print('%d월은 봄입니다.'%month)
# if month=='6' or month=='7' or month=='8' :
#     print('%d월은 여름입니다.'%month)
# if month=='9' or month=='10' or month=='11' :
#     print('%d월은 가을입니다.'%month)
# if month=='12' or month=='1' or month=='2' :
#     print('%d월은 겨울입니다.'%month)


# a=input('주민번호 뒷자리 첫 번째 숫자를 입력해주세요.:')
# if a=='1' or a=='3' :
#     print('남성입니다!')
# if a=='2' or a=='4' :
#     print('여성입니다!')

# 문제풀기

# x=int(input('양의 정수를 입력하세요.:'))

# if x%2==0 :
#     print('짝수이다!')
# else :
#     print('홀수이다!')

# pilgi=int(input('필기시험 점수는?:'))
# silgi=int(input('실기시험 점수는?:'))
# if pilgi>=80 and silgi>=80 :
#     result='합격'
# else :
#     result='불합격'
# print('-필기시험 점수:%d'%pilgi)
# print('-실기시험 점수:%d'%silgi)
# print('-판정:%s'%result)

# somunja=input('영문 소문자 하나를 입력하세요.:')
# if somunja=='a' or somunja=='e' or somunja=='i' or somunja=='o' or somunja=='u' :
#     print('%s는 모음이다.'%somunja)
# else :
#     print('%s는 자음이다.'%somunja)

# a='apple'
# b=a.upper()
# print(b)

# somunja=input('영문 대문자 또는 소문자 하나를 입력하세요:')
# damunja=somunja.upper()
# if damunja=='A' or damunja=='E' or damunja=='I' or damunja=='O' or damunja=='U' :
#     print('%s->모음'%damunja)
# else :
#     print('%s->자음'%damunja)

# height=int(input('키는?'))
# weight=int(input('몸무게는?'))
# a=(height-weight)*0.9
# print('='*50)
# print('키:',height)
# print('몸무게:',weight)
# if weight>a :
#     print('건강을 위해 다이어트가 필요합니다!')
# else :
#     print('표준 또는 마른 체형입니다!')

# print('아르바이트 급여 계산 프로그램')
# print('*시급')
# print('-주간 근무:9,500원')
# print('-야간 근무:주간 시급*1.5')
# print()

# hour_pay=9500

# a=int(input('1(주간 근무) 또는 2(야간 근무)을 입력해주세요:'))
# work_time=int(input('근무 시간을 입력해주세요:'))
# if a==1 :
#     day_night='주간'
#     pay=hour_pay*work_time
# else :
#     day_night='야간'
#     pay=hour_pay*work_time*1.5
# print('%s시간 동안 일한 %s 급여는 %d원 입니다.'%(work_time,day_night,pay))

# score=int(input('점수는?'))
# if score>=90 :
#     grade='A'
# elif score>=80 :
#     grade='B'
# elif score>=70 :
#     grade='C'
# elif score>=60 :
#     grade='D'
# else :
#     grade='F'

# print('등급:',grade)

# print('기능 선택')
# print('1. 더하기')
# print('2. 빼기')
# print('3. 곱하기')
# print('4. 나누기')
# print()

# g=input('계산기 기능을 선택하세요(1/2/3/4):')
# num1=int(input('첫 번째 숫자를 입력하세요:'))
# num2=int(input('두 번째 숫자를 입력하세요:'))
# if g=='1' :
#     print('%d+%d=%d'%(num1,num2,num1+num2))
# elif g=='2' :
#     print('%d-%d=%d'%(num1,num2,num1-num2))
# elif g=='3' :
#     print('%d*%d=%d'%(num1,num2,num1*num2))
# elif g=='4' :
#     print('%d/%d=%d'%(num1,num2,num1/num2))
# else :
#     print('입력 숫자가 잘못 되었습니다!')
    
