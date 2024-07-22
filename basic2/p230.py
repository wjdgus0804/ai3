animals=('토끼','거북이','사자','여우')
print(animals)
numbers=tuple(range(10))
print(numbers)

# 출력하기
print(animals[1:])
print(numbers[:3])

# 수정하기
# animals[2]='호랑이'  수정X

anNu=animals+numbers
print(anNu)

# for문
s=0
n2=tuple(range(101))
for i in n2:
    s=s+i
print(s)
print(sum(n2))
