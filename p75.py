'''year=2024
month=7
day=12
print(year,month,day,sep='-')

hp1='010'
hp2='3346'
hp3='5238'

price=1000
print(price,'원', sep='')


print('안녕하세요\n반갑습니다')
print('안녕하세요\t반갑습니다')
print('\\')
print('\'')
print('\"')

# '안녕'
print('\'안녕\'')

# "안녕"
print('\"안녕\"')

# p80 퀴즈
kor=input('국어 성적을 입력하세요:')
eng=input('영어 성적을 입력하세요:')
math=input('수학 성적을 입력하세요:')

sum=int(kor)+int(eng)+int(math)
avg=sum/3
print('합계:%d, 평균:%.2f'%(sum,avg))
'''

# 코딩 연습
'''
# 1
year=input('년은?')
month=input('월은?')
day=input('일은?')
print(year,month,day,sep='.')

# 2
width=int(input('사각형의 너비는?'))
height=int(input('사각형의 높이는?'))
length=2*width+2*height
area=width*height
print('사각형의 너비:%dcm'%width)
print('사각형의 높이:%dcm'%height)
print('둘레 길이:%dcm'%length)
print('면적:%dcm2'%area)

# 3
r=float(input('반지름을 입력하세요:'))
length=2*r*3.14
area=r*r*3.14
print('반지름:%.2f'%r)
print('원의 둘레:%.2f'%length)
print('원의 면적:%.2f'%area)

# 4
inch=float(input('인치는?'))
cm=inch*2.54
print('27.0inch=>%.1fcm'%cm)
'''

#5
price=int(input('책 값은?:'))
dis=int(input('할인율은?:'))
deli=int(input('배송료는?'))
pay=price-(price*(dis/100))+deli
print('책 값:%d원'%price)
print('할인율:%d'%dis)
print('배송료:%d원'%deli)
print('결제 금액:%d원'%pay)








