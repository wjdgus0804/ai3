# num=int(input('수를 입력하세요:'))
# if num>=0 and num<=9 :
#     print('%d는 한 자리 숫자이다.'%num)
# elif num>=10 and num<=99 :
#     print('%d는 두 자리 숫자이다.'%num)
# elif num>=100 and num<=999 :
#     print('%d는 세 자리 숫자이다.'%num)
# else :
#     print('오류! %d는 범위(0~999) 이외의 숫자이다.'%num)

# number=input('수를 입력하세요:')
# inputLength=len(number)
# number=int(number)
# if inputLength==1 :
#     print('%d는 한 자리 숫자이다.')
# elif inputLength==2 :
#     print('%d는 두 자리 숫자이다.')
# elif inputLength==3 :
#     print('%d는 세 자리 숫자이다.')
# elif not(0<=number<=999) :
#     print('오류! %d는 범위(0~999) 이외의 숫자이다.')


# num1=int(input('첫 번째 숫자를 입력하세요:'))
# num2=int(input('두 번째 숫자를 입력하세요:'))
# print('원하는 연산은?')
# a=input('+,-,*,/ 중 하나를 선택하세요:')
# if not(a=='+' or a=='-' or a=='*' or a=='/') :
#     print('선택 오류!')
# elif a=='+' :
#     print('%d+%d=%d'%(num1,num2,num1+num2))
# elif a=='-' :
#     print('%d-%d=%d'%(num1,num2,num1-num2))
# elif a=='*' :
#     print('%d*%d=%d'%(num1,num2,num1*num2))
# elif a=='/' :
#     print('%d/%d=%d'%(num1,num2,num1/num2))


# time1=int(input('첫 번째 시간의 시를 입력하세요:'))
# time2=int(input('첫 번째 시간의 분을 입력하세요:'))
# time3=int(input('두 번째 시간의 시를 입력하세요:'))
# time4=int(input('두 번째 시간의 분을 입력하세요:'))
# if not(0<=time1<=24 or 0<=time3<=24 or 0<=time2<=59 or 0<=time4<=59) :
#     print('시간과 분을 잘못 입력하셨어요')
# elif time1<=time3 :
#     print('-빠른 시간:%d:%d'%(time1,time2))
#     print('-느린 시간:%d:%d'%(time3,time4))
# elif time1==time3 and time2<time4 :
#     print('-빠른 시간:%d:%d'%(time1,time2))
#     print('-느린 시간:%d:%d'%(time3,time4))
# elif time1==time3 and time2>time4 :
#     print('-빠른 시간:%d:%d'%(time3,time4))
#     print('-느린 시간:%d:%d'%(time1,time2))
# else :
#     print('-빠른 시간:%d:%d'%(time3,time4))
#     print('-느린 시간:%d:%d'%(time1,time2))




