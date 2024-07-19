'''# 정렬
data=[12,8,15,32,-3,-20,15,34,6]
print(data)
data.sort()
print(data)

data2=['a','가','@','1','ac']
print(data2)
data2.sort() # 오름차순 정렬 유니코드 순서대로 정렬 
print(data2)
# 내림차순 정렬 하기
data2.sort(reverse=True)
print(data2)
# 오름차순 정렬
data2.sort(reverse=False)
print(data2)



# p205
string1='사과는 맛있다. 나는 사과를 제일 좋아한다.'
print(string1)

x=string1.replace('사과','딸기')
print(x)

# hello='have-a-nice-day'
# print(hello)
# list1=hello.split(' ')
# print(list1)
# print(type(list1))
# for i in range(0,len(list1)) :
#     print('list1[%d]: %s'%(i,list1[i]))

list1='a,b,c,d,e,f'
list1Sp=list1.split(',')
print(list1Sp)
list22=[]
list2=['홍길동:100:20','이순신:90:80','최수연:100:75']
for i in list2 :
    list10=i.split(':')
    print(list10)
    for j in list10 :
        list22.append(j)
print(list22)

# 나누세요
list55=[]
list5=['kbs-사장-200, mbc-부장-100','kbs-사원-50, sbs-대리-80']
for i in list5 :
    list50=i.split('-')
    print(list50)
    for j in list50 :
        list05=j.split(',')
        print(list05)
        for k in list05 :
            list55.append(k)
print('완성==>%s'%list55)


# ----------------
# 데이터를 사이트에서 검색해오기
import requests as req
url='http://search.naver.com/search.naver'
rData=req.get(url,params={'query':'백일해 증상'})
print(rData.text)


# p201

names=['a','b','c']
x='-'.join(names)
print(x)

# p212 2차원 리스트
list2D=[[1,2],[3,4,5],[1]]
print(list2D[1][1]) # 4
print(list2D[0][1]) # 2

list2DD=[[1,2,3,4],[5,6,7]]
print(list2DD[0][0],end=' ')
print(list2DD[0][1],end=' ')
print(list2DD[0][2],end=' ')
print(list2DD[0][3],end=' ')
print()
print(list2DD[1][0],end=' ')
print(list2DD[1][1],end=' ')
print(list2DD[1][2],end=' ')
print()

print(len(list2DD))
print(len(list2DD[0]))
print(len(list2DD[1]))

for i in range(0,(len(list2DD))) :
    for j in range(0,len(list2DD[i])) :
        print(list2DD[i][j],end=' ')
    print()


list3D=[[[1,2,3],[4,5]],[[6,7],[8]]]
print(list3D[1][1][0])  # 8 출력
print(list3D[0][0][0])  # 1 출력
'''

# qu=['s_hool','compu_er','deco_ation','windo_','hi_tory']
# an=['c','t','r','w','s']
# for i in range(len(qu)) :
#     q='%s:밑 줄에 들어갈 알파벳은?'%qu[i]
#     guess=input(q)
#     if guess==an[i] :
#         print('정답!')
#     else :
#         print('틀렸어요!')

# scores=[]
# while True:
#     x=int(input('성적을 입력하세요(종료 시 -1 입력): '))
#     if x==-1 :
#         break
#     else :
#         scores.append(x)
    
# sum=0
# for score in scores :
#     sum=sum+score
# avg=sum/len(scores)
# print('합계:%d, 평균:%.2f'%(sum,avg))

# s=[91,94,100,87,89,86,85,84,83,79,78,77,69,68,67,66,55,54,53,52]
# soo=0
# woo=0
# mi=0
# yang=0
# ga=0

# i=0
# while i<len(s) :
#     if 90<=s[i]<=100 :
#         soo=soo+1
#     if 80<=s[i]<=89 :
#         woo=woo+1
#     if 70<=s[i]<=79 :
#         mi=mi+1
#     if 60<=s[i]<=69 :
#         yang=yang+1
#     if 0<=s[i]<59 :
#         ga=ga+1
#     i=i+1
# print('수:%d명'%soo)
# print('우:%d명'%woo)
# print('미:%d명'%mi)
# print('양:%d명'%yang)
# print('가:%d명'%ga)

# seats=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0],[0,1,0,0,0,1,0,1,0,0],[0,0,0,0,0,0,1,0,0,0],[1,0,1,0,0,0,0,0,0,1]]
# for i in range(len(seats)) :
#     for j in range(len(seats[i])) :
#         if seats[i][j]==0 :
#             print('%3s'%'ㅇ',end=' ')
#         else :
#             print('%3s'%'ㅁ',end=' ')
#     print()
