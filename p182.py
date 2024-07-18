# list1=[3,15,-12.5,'사과','딸기',True,False]
# list2=list(range(1,21,2))
# print(list1)
# print(list2)
# print(list1[4])
# for i in range(7) :
#     print(list1[6-i],end=' ')
# print()
# print(list2[-1])
# print(list2[-4:])
# print(list2[: :2])
# print(list2[-1: :-2])

# 100 110 120 ... 200
# count=0
# list3=list(range(100,201,10))
# print(list3)
# for i in list3 :
#     count=count+1
# print()
# print('답은:%d개'%count)

# sum=0
# for i in list3 :
#     sum=sum+i
# print('합계:%d'%sum)

# print(len(list3))

# # p185
# colors=['빨간색','파란색','노란색','검정색','초록색']

# for color in colors :
#     print('나는 %s을 좋아한다.'%color)

# n=len(colors)
# for i in range(0,n):
#     print('나는 %s을 좋아한다.'%colors[i])

# animals=['코끼리','호랑이','사슴','펭귄','여우']
# i=0
# while i<len(animals) :
#     print(animals[len(animals)-1-i])
#     i=i+1

# 성적 프로그램 만들기
# list1=['홍길동',100,80]
# list2=['이순신',90,75]
# list3=['최경미',75,100]
# print('이름    국어 점수    수학 점수    합계    평균')
# print(list1[0],'    ', list1[1],'    ', list1[2],'    ', list1[1]+list1[2],'    ', (list1[1]+list1[2]/2))
# print(list2[0],'    ', list2[1],'    ', list2[2],'    ', list2[1]+list2[2],'    ', (list2[1]+list2[2]/2))
# print(list3[0],'    ', list3[1],'    ', list3[2],'    ', list3[1]+list3[2],'    ', (list3[1]+list3[2]/2))

# # 우리반 이름: 홍길동, 이순신, 최경미
# print('우리반 이름:', list1[0],',',list2[0],',',list3[0])

# 우리반 국어 점수 합계:
# 우리반 영어 점수 합계:
# 우리 반에서 국어를 제일 잘 본 사람의 이름은? 홍길동

# print('우리반 국어 점수 합계: %d'%(list1[1]+list2[1]+list3[1]))
# print('우리반 수학 점수 합계: %d'%(list1[2]+list2[2]+list3[2]))

# if list1[1]>list2[1] and list1[1]>list3[1]:    # list1이 제일 큰 경우
#     print('우리 반에서 국어 점수가 제일 높은 사람의 이름은?:%s'%list1[0])
# elif list2[1]>list1[1] and list2[1]>list3[1]:
#     print('우리 반에서 국어 점수가 제일 높은 사람의 이름은?:%s'%list2[0])
# elif list3[1]>list1[1] and list3[1]>list2[1]:
#     print('우리 반에서 국어 점수가 제일 높은 사람의 이름은?:%s'%list3[0])

# or

# if list1[1]>list2[1] and list1[1]>list3[1]:    # list1이 제일 큰 경우
#     topKorName=list1
# elif list2[1]>list1[1] and list2[1]>list3[1]:
#     topKorName=list2
# elif list3[1]>list1[1] and list3[1]>list2[1]:
#     topKorName=list3
#     print('우리 반에서 국어 점수가 제일 높은 사람의 이름은?:%s'%topKorName[0])

# findName=input('찾고 싶은 사람은?')
# if findName==list1[0] or findName==list2[0] or findName==list3[0] :
#     print('우리반에 %s 있어요.'%findName)
# else :
#     print('우리반에 %s 없어요.'%findName)

# list 하나 더 추가하기


