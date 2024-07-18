
'''name=input('이름은')
print(name)

age=input('당신의 나이는?')
print('당신의 나이는 %s살입니다'%age)
print('당신의 나이는 %d살입니다'%int(age))


# 입력: 당신이 태어난 년도? 

year=input('당신이 태어난 년도는?')
age = 2024-int(year)
print('당신의 나이는 %d살입니다.'%int(age))


# p73 퀴즈
a=input('첫 번째 정수를 입력하세요:')
b=input('두 번째 정수를 입력하세요:')
c=a+b
print(c)

a=input('첫 번째 정수를 입력하세요:')
b=input('두 번째 정수를 입력하세요:')
c=int(a)+int(b)
print(c)


a=input('첫 번째 정수를 입력하세요:')
b=input('두 번째 정수를 입력하세요:')
aVal=int(a)
bVal=int(b)

if aVal>bVal :
    print(aVal)
else : 
    print(bVal)

if aVal>=bVal :
    print(aVal)
else :
    print(bVal)
    
if aVal<bVal :
    print(aVal)
else :
    print(bVal)


a=input('첫 번째 정수를 입력하세요:')
b=input('두 번재 정수를 입력하세요:')
c=input('세 번재 정수를 입력하세요:')
aVal=int(a)
bVal=int(b)
cVal=int(c)

if bVal>aVal>cVal :
    print(bVal)
else :
    print(cVal)
'''
    
a=int(input('첫 번째 정수를 입력하세요:'))
b=int(input('두 번째 정수를 입력하세요:'))
c=int(input('세 번째 정수를 입력하세요:'))

if a>b and a>c :
    print(a)
elif b>a and b>c :
    print(b)
elif c>a and c>b :
    print(c)



