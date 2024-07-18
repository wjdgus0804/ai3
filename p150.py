# word='I am happy'
# for i in word:
#     print(i,end='')

# phone='010-3346-5238'
# print(phone)

# # 핸드폰 번호 안에 7이 있나요? 답 없습니다.
# flag=0
# for i in phone :
#     if i=='0' :
#         flag=1
# if flag==0 :
#         print('없습니다.')
# else :
#      print('있습니다.')

# 영어 문장에 'a' 글자가 있나요?
for j in range(0,3,1) :
    flag=0
    word='apple'
    for i in word :
        if i=='a' :
            flag=1
    if flag==0 :
        print('없어요')
    else :
        print('1개 있어요')

    # 답은 1개 있어요
    flag=0
    word='an/a'
    for i in word :
        if i=='a' :
            flag=2
    if flag==0 :
        print('없어요')
    else :
        print('2개 있어요')
        
    # 답은 2개 있어요
    flag=0
    word='book'
    for i in word :
        if i=='a' :
            flag=0
    if flag==0 :
        print('없어요')
    else :
        print('2개 있어요')

    # 답은 없어요



