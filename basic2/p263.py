# def average(*args) :
#     print(len(args))
# def func(food) :
#     for x in food :
#         print(x,end=' ')
    
    
# average(85,96,87) # 함수 호출
# average(77,93,85,97,72)


# fruits=['사과','오렌지','바나나']
# func(fruits)

# def say_hello(name) :
#     print('%s님 안녕하세요!'%name)

# say_hello('홍지수')
# say_hello('안지영')
# say_hello('황예린')

# def print_name(first_name,last_name) :
#     name=first_name+last_name
#     print('이름:',name)

# print_name('홍','정원')

# def even_odd(n) :
#     if n%2==0 :
#         print('%d는 짝수이다.'%n)
#     else :
#         print('%d는 홀수이다.'%n)

# x=int(input('양의 정수를 입력하세요:'))
# even_odd(x)

# def average(*args) :
#     num_args=len(args)
#     sum=0
#     for i in range(num_args) :
#         sum=sum+args[i]
#     avg=sum/num_args
#     print('%d과목 평균: %.1f'%(num_args,avg))
# average(85,96,87) # 함수 호출
# average(77,93,85,97,72)

# def add(a,b) :
#     c=a+b
#     print('%d+%d=%d'%(a,b,c))

# add(12,15)
# add(245,300)
# add(-38,-12)

# def sum_int(start,end) :
#     sum=0
#     for i in range(start,end+1) :
#         sum=sum+i
#     print('%d~%d 정수 합계: %d'%(start,end,sum))
# sum_int(20,50)
# sum_int(600,800)

# def member_join(*args) :
#     result=' '
#     for arg in args :
#         result=result+arg+' '
#     print('가입 회원:',result)
# member_join('김정연','안서영')
# member_join('황선형','김철영','이창연')
# member_join('정수진','김보람','정수연','함소영')

# def multiply(num,x) :
#     i=0
#     while i<len(num) :
#         num[i]=num[i]*x
#         i=i+1

# numbers=[10,20,30,40,50]
# multiply(numbers,10)
# print(numbers)
# multiply(numbers,10)
# print(numbers)
