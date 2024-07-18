# 200 숫자를 15번 반복해서 출력하기
n200=200
print(str(n200)*15)

# 64쪽 퀴즈 1번
x='수학 성적:'
print(type(x))
y='80'
print(type(y))
z=x+str(y)
print(type(z))

date='20220301'
year=date[0:4]
month=date[4:6]
day=date[6:]
date2=year+'-'+month+'-'+day
print(date2)

print(len(date))

# 자기 이름을 8 번 반복하기 
# 결과: 김정현김정현김정현김정현김정현김정현김정현김정현
name='김정현'
print(str(name)*8)

# 1단계 
name= '김정현'
# 2단계
num='010-3346-5238'
# 3단계
lastNum=num[-1]
endNum=int(lastNum)
print(name*endNum)

name='김정현'
birth='20010804'
lastNum=birth[-1]
endNum=int(lastNum)
print(name*endNum)


phone1='82-01-336-5238'
# 15글자이면 한국 핸드폰번호
phone2='82-01-336-5238'
# 15글자 아니면 한국집번호

# 결과1: phone1은 한국 핸드폰번호입니다.
# 결과2: phone2은 한국 집번호입니다.

'''
if len(phone1)==15:
    print('phone1은 한국 핸드폰번호입니다.')
else :
    print('phone1는 한국 집번호입니다.')

if len(phone2)==15:
    print('phone2은 한국 핸드폰번호입니다.')
else :
    print('phone2는 한국 집번호입니다.')
'''

# 핸드폰 , 핸드폰 일 때

if len(phone1)==15 and len(phone2)==15 :
    print('phone1은 핸드폰번호입니다.')
    print('phone2는 핸드폰번호입니다.')
elif len(phone1)==15 and len(phone2)==15 :
    print('phone1은 핸드폰번호입니다.')
    print('phone2는 핸드폰번호입니다.')

# 핸드폰, 집 일 때

if len(phone1)==15 and len(phone2)==15 :
    print('phone1은 핸드폰번호입니다.')
    print('phone2는 핸드폰번호입니다.')
elif len(phone1)==15 and len(phone2)==14 :
    print('phone1은 핸드폰번호입니다.')
    print('phone2는 집번호입니다.')

# 집, 핸드폰 일 때

if len(phone1)==15 and len(phone2)==15 :
    print('phone1은 핸드폰번호입니다.')
    print('phone2는 핸드폰번호입니다.')
elif len(phone1)==14 and len(phone2)==15 :
    print('phone1은 집번호입니다.')
    print('phone2는 핸드폰번호입니다.')

# 집, 집 일 때

if len(phone1)==15 and len(phone2)==15 :
    print('phone1은 핸드폰번호입니다.')
    print('phone2는 핸드폰번호입니다.')
elif len(phone1)==14 and len(phone2)==14 :
    print('phone1은 집번호입니다.')
    print('phone2는 집번호입니다.')





animal='고양이'
catName='로드'
x='나는 %s %s를 좋아합니다.'%(animal, catName)
print(x)

age=24
print('내 나이는 %d살 입니다.'%age)

pay=100000000
# 내 나이는 24살이고 연봉은 100000000원입니다.
print('내 나이는 %d살이고 연봉은 %d원입니다.'%(age,pay))


kor=88
eng=95
math=97
sum=kor+eng+math
avg=sum/3
print('합계:%d, 평균:%.0f'%(sum, avg))



'''name=input('이름은')
print(name)

age=input('당신의 나이는?')
print('당신의 나이는 %s살입니다'%age)
print('당신의 나이는 %d살입니다'%int(age))
'''

# 입력: 당신이 태어난 년도? 

year=input('당신이 태어난 년도는?')
age = 2024-int(year)
print('당신은 %d살입니다.'%int(age))


