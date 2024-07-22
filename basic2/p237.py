# # 딕셔너리
# member={'name':'황예린','age':22,'email':'yerin@hamail.net','age':30}
# print(member)
# # 이름
# print(member['name'])
# # 나이
# print(member['age'])
# # 이메일
# print(member['email'])

# score=dict([('국어',80),('영어',90),('수학',100)])
# print(score)
# print(score['국어'])
# score['국어']=90
# print(score,'!!!')

# score2=dict([['국어',80],['영어',90],['수학',100]])
# print(score2)
# print(score2['수학'])
# score2['국어']=90
# print(score2,'@@@')

# user= {'id':'kim55','name':'강성준','level':7,'point':10000}
# print(user)
# print(user['id'])
# print(user['name'])
# print(user['point'])

# scores={'kor':90,'eng':89,'math':98}
# print(scores)
# scores['music']=100
# print(scores)

# word={'door':'문','chair':'의자','table':'책상','house':'집'}
# print(word)
# word['table']='테이블'
# print(word)
# word['house']='하우스'
# print(word)

# car={'brand':'현대','model':'아반떼','start':1990,'year':2021}
# print(car)
# x=car.pop('start')
# print(x)
# print(car)

# car={'brand':'현대','model':'아반떼','start':1990,'year':2021}
# car.clear()
# print(car)

# area_code={'서울':'02','부산':'051','대구':'053','광주':'062'}
# for key in area_code :
#     print('%s 지역번호: %s'%(key,area_code[key]))

# scores={'김채린':85,'박수정':98,'함소희':94,'안예린':90,'연수진':93}
# sum=0
# for key in scores :
#     sum=sum+scores[key]
#     print('%s : %d'%(key,scores[key]))

# avg=sum/len(scores)
# print('합계:%d, 평균:%.2f'%(sum,avg))

# admin_info={'id':'admin','password':'12345'}
# inputId=input('아이디를 입력하세요:')
# inputPw=input('비밀번호를 입력하세요:')

# if inputId=='admin' and inputPw=='12345' :
#     print('정보에 접근 권한이 있습니다!')
# else :
#     print('정보에 접근 권한이 없습니다!')

# word={'꽃':'flower','나비':'butterfly','학교':'school','자동차':'car','비행기':'airplane'}
# print()
# print('<영어 단어 맞추기 퀴즈>')
# for kor in word :
#     wordQ=input("'%s'에 해당되는 영어 단어를 입력해주세요:"%kor)
#     if wordQ==word[kor] :
#         print('정답입니다!')
#     else :
#         print('틀렸습니다!')

# year_sale={'2016':237,'2017':98,'2018':158,'2019':233,'2020':120}
# for key in year_sale :
#     if key=='2017' :
#         print('%s년 자동차 판매량: %d대'%(key,year_sale[key]))

# year_sale={'2016':237,'2017':98,'2018':158,'2019':233,'2020':120}
# sum=0
# for key in year_sale:
#     if key=='2018' or key=='2019' :
#         print('%s년 자동차 판매량: %d'%(key,year_sale[key]))
#         sum=sum+year_sale[key]

# print('2년간 자동차 판매량: %d대'%sum)

year_sale={'2016':237,'2017':98,'2018':158,'2019':233,'2020':120}
