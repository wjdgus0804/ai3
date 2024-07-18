# for i in range(5) :
#     phone=input('하이픈(-)을 포함한 휴대폰 번호를 입력하세요:')

#     for i in phone :
#         if i !='-' :
#             print('%s'%i,end='')
#     print()


# 1단계 키보드로 입력을 받는다.
# 2단계 한 글자씩 가져와서 숫자인지 비교한다.
# 3단계 숫자이면 출력한다, 아니면 다시 2단계로 간다.

# phone=input('휴대폰 번호를 입력하세요:')
# for i in phone :
#     if '0'<=i<='9' :
#         print('%s'%i,end='')

# # 대문자만 출력
# phone=input('휴대폰 번호를 입력하세요:')
# for i in phone: 
#     if 'A'<=i<='Z' :
#         print('%s'%i,end='')
# # 소문자
# phone=input('휴대폰 번호를 입력하세요:')
# for i in phone: 
#     if 'a'<=i<='z' :
#         print('%s'%i,end='')


# phone=input('휴대폰 번호를 입력하세요:')
# for i in phone: 
#     if not('A'<=i<='Z' or 'a'<=i<='z' or '0'<=i<='9') :
#         print('%s'%i,end='')
    

# print('-'*30)
# print(' 섭씨  화씨')
# print('-'*30)
# for c in range(-20,31,5) :
#     f=c*9.0/5.0+32.0
#     print('%5d %6.1f'%(c,f))
# print('-'*30)

# cnt=0
# for i in range(200,801): 
#     if i%5!=0 :
#         print('%d'%i,end=' ')
#         cnt=cnt+1
#     if cnt%10==0 :
#         print()


# print('-'*40)
# print('     cm     mm      m     inch')
# print('-'*40)
# for cm in range(1,101) :
#     mm=cm*10.0
#     m=cm*0.01
#     inch=cm*0.3937
#     print('%7d %7d %7.2f %7.1f'%(cm,mm,m,inch))

# print('-'*40)


num=input('숫자를 입력하세요:')
cnt=0
for i in num :
    i=int(i)
    if i%2==1 :
        cnt=cnt+1
print('홀수의 개수: %d개'%cnt)




# 추가로 내용을 넣었다.

