# 입력받기 '477569040'
# 입력받은 문자(숫자)를 1개씩 가져다가 '4'
# 문자를 숫자로 변경한다. '4'--> 4
# 홀수인지 판단한다. 5%2==1
# 갯수 세기 cnt=cnt+1

'''
num=input('숫자를 입력하세요:')
cnt=0
for i in num :
    i=int(i)
    if i%2==1 :
        cnt=cnt+1
    
print('홀수의 개수:%d개'%cnt)


# 10 20 30 ... 100까지  출력하기
for k in range(5) :
    for i in range(10,101,10) :
        print(i,end=' ')
    print()
'''

for k in range(5) :
    for i in range(1, 6-k , 1) :
        print(i,end=' ')
    print()
    

        



