# 1~200까지 출력

# for문
# for i in range(1,201) :
#     if i==100 :
#         continue
#     print(i,end=' ')
    

# print()
# print('-'*100)
# # while문
# i=1
# while i<200 :
#     i=i+1
#     if i==100 :
#         continue
#     print(i,end=' ')
    
    
# 100이면 빠지기
# 100이면 찍지 않고 건너 뛰기(반복문 계속) 101 찍기

# n=1
# sum=0
# count=0

# while n<=100 :
#     if n%2==1 :
#         sum=sum+n
#         print('%6d'%sum,end=' ')
#         count=count+1

#     if count%10==0 :
#         print()
#     n=n+1


# print('-'*30)
# print(    '달러   원화   유로')
# print('-'*30)

# dollar=10

# while dollar<=100 :
#     won=dollar*1080
#     euro=dollar*0.81
#     print('%4d%8.0f%7.1f'%(dollar,won,euro))
#     dollar=dollar+10

# print('-'*30)


# s=input('문장을 입력해 주세요:')
# i=len(s)-1
# while i>=0 :
#     if s[i]==' ' :
#         print('-',end='')
#     else :
#         print('%s'%s[i],end='')
#     i=i-1


# for i in range(1,11):
#     if i%2==1 :
#         print(i)


# sum=0
# for i in range(1,101) :
#     if i%3==0 :
#         sum=sum+i
# print('1~100 까지의 3의 배수 합계:%d'%sum)
    

# for i in range(1,101) :
#     if i%5==0 :
#         print(i,end=' ')
        

# sum=0
# for i in range(1,101) :
#     if i%4==0 :
#         sum=sum+i
#         print(i,'-->',sum)

# fact=1
# for i in range(1,10) :
#     fact=fact*i
# print('10!=%d'%fact)

# print('-'*40)
# print('  cm   mm   m   inch')
# print('-'*40)

# for cm in range(1,51) :
#     mm=cm*10
#     m=cm*0.01
#     inch=cm*0.39
#     print('%4d%5d%7.2f%7.2f'%(cm,mm,m,inch))
# print('-'*40)

# 소수 구하기

# start=int(input('시작 수를 입력하세요:'))
# end=int(input('끝 수를 입력해주세요:'))
# for x in range(start,end+1) :
#     for i in range(2,x) :
#         if x%i==0 :
#             break
#         if x==i+1 :
#             print('%d'%x,end=' ')

    

for i in range(1,10) :
    print('')
