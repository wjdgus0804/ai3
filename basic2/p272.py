# def func(c) :
#     x=c+5
#     return x
# r=func(100)
# print(r)

# def inchToCm(inch) :
#     cm=[]
#     for i in range(inch,31,10) :
#         k=i*2.54
#         cm.append(k)
#     return cm

# result=inchToCm(10)
# print(result)


def p(num) :
    result=[]
    a=1
    for i in range(num,0,-1) :
        a=a*i
    result.append(a)
    a=0
    for i in range(1,num+1) :
        a=a+i
    result.append(a)
    a=0
    for i in range(1,num+1) :
        a=a+1
    result.append(a)
    return result
print(p(5))




print(p(5))  # 결과 120 5!(5*4*3*2*1)
# 결과 5!-120, 1~5까지 합-15, 1~5까지 길이-5



