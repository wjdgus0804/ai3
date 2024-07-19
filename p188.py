nameList=['a','b']
noList=list(range(241001,241021))
print(noList)
print(nameList[1])
for i in noList :
    print(i,end=' ')
print()
i=0
while i<len(noList) :
    print(noList[i],end=' ')
    i=i+1

print()

nameList = ['이순신','홍길동','박수연']
# 박수연을 박수현으로 바꾸기
nameList[2]='박수현'
for i in nameList :
    print(i,end=' ')
print()
# 정현희를 추가하기
nameList.append('정현희')
for i in nameList :
    print(i,end=' ')
print()
# 이순신 홍길동 박수현 정현희
# 이순신 이승후 홍길동 박수현 정현희   삽입하기
nameList.insert(1,'이승후')
for i in nameList:
    print(i,end=' ')
print()
# 이순신 이승후 홍길동 박수현 정현희
# 박수현이 몇 번째 인덱스에 있는지? 답:3
# index()
try : 
    nameList=['박수현','이순신''이승후','홍길동','정현희']
    searchIndex=nameList.index('박수현',0,10)  # 0번 인덱스부터 9번 인덱스까지
    print(searchIndex)
    searchIndex=nameList.index('장수현',0,10)  # 0번 인덱스부터 9번 인덱스까지
    print(searchIndex)
except ValueError :
    print('장수현은 리스트에 없습니다.')

# p194
number=[1,2,3,4,2,2,2,2]
number.remove(2) # 값 2가 삭제
print(number)

number=[1,2,3,4,2,2,2,2]
number.pop(2) # 2번 인덱스가 삭제
print(number)

number.clear()
print(number)

# p199
p1=[1,3,5]
p2=[2,4,6]
p3=p1+p2
print(p3)

p4=list(range(1,11))
print(p4)
p4Sum=sum(p4)
print(p4Sum)

# sum=0
# for i in p4:
#     sum=sum+i
# print(sum)

p5=[100,8,90]
p5Sum=sum(p5)
print(p5Sum)
p5Avg=p5Sum/len(p5)
print(p5Avg)
p5Max=max(p5)
print(p5Max)

p5.reverse()
print(p5)
p5.reverse()
print(p5)

p6=['apple','banana','orange']
print(p6,'!!!')
p6Copy=p6.copy()
print(p6Copy,'~~~')

# p6의 리스트 apple 삭제하기
p6.remove('apple')
print(p6,'!!!')
print(p6Copy,'~~~')

# p6Copy 'orange'를 'mango' 로 바꾸기
p6Copy[2]='mango'
print(p6Copy,'~~~')

p7=['apple','banana','orange']
p77=p7  # 얕은 복사: p7의 주소가 p77로 복사된다. p7이나 p77을 변경하면 같이 변경됨.
print(p7)
print(p77)
# p7에 있는 'apple' 삭제하기
# p77에 있는 'orange' 를 'mango'로 변경하기
# p7에 'bear' 추가하기

p7.remove('apple')
print(p7)
print(p77)
p77[1]='mango'
print(p7)
print(p77)
p7.append('bear')
print(p7)
print(p77)
