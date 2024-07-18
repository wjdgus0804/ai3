'''# 키보드로 이름을 입력 받아보세요.
name=input('이름은?:')
# 이름을 화면에 출력해보세요.
print('입력한 이름은 %s입니다.'%name)
# 키보드로 점수를 입력 받아보세요.
point=input('포인트 점수는?:')
# 포인트 점수의 20%는 600점입니다.
# 1단계 문자형 '3000'을 숫자형으로 변환하기
pointValue=int(point)
# 2단계 계산하기 
point20=pointValue*0.2
# 3단계 출력하기
print('포인트 점수의 20%','는 %d점입니다.'%point20,sep='')
'''

# 당신의 주소는? 강북구 수유동
address=input('당신의 주소는?:')
print(address*10)

# 몇 번 반복할래요? 5
address2=input('당신의 주소를 몇 번 반복할래요?:')
print()

# 출력 당신의 주소의 글자는 7글자 입니다.
address3=len(address)
print('당신의 주소의 글자는 %d글자입니다.'%address3)





