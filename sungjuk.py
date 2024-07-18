name=[]
kor=[]
eng=[]
math=[]
menu='1'
while menu!='5' :
    print('-'*30)
    print('성적관리 프로그램')
    print('-'*30)
    print('1. 학생 이름 삽입하기')
    print('2. 성적 입력하기')
    print('3. 통계자료 보기')
    print('4. 학생 자료 삭제하기')
    print('5. 프로그램 종료하기')
    menu=input('===> 메뉴를 선택하세요 (1/2/3/4/5):')
    if menu=='1' :
        # 학생 이름 삽입하기 
        n=input('학생의 이름은?:') #홍길동
        name.append(n)
        print(name) # 나중에 지울 것.
    elif menu=='2' :
        # 성적 입력하기 
        k=int(input('국어 점수는?:'))
        e=int(input('영어 점수는?:'))
        m=int(input('수학 점수는?:'))
        kor.append(k)
        eng.append(e)
        math.append(m)
        print(kor,eng,math)
    elif menu=='3' :
        # 통계자료 보기 ??
        print('1) 반 전체 성적 검색')
        print('2) 개인 점수 검색')
        print('3) 통계 자료 나가기')
        stMenu=input('번호를 선택하세요(1/2/3)')
        if stMenu=='1' :
            # 반 전체 통계
            print('-'*30)
            print(' 이름    국어    영어    수학')
            print('-'*30)
            for i in range(len(name)) :
                print('%s   %d   %d   %d'%(name[i],kor[i],eng[i],math[i]))
        elif stMenu=='2' :
            # 학생 1명 자료
            findName=input('점수를 알고 싶은 학생 이름은?:')
            try :
                findIndex=name.index(findName)
                print('%s %d %d %d'%(name[findIndex],kor[findIndex],eng[findIndex],math[findIndex]))
            except ValueError :
                print('%s 우리반 학생이 아닙니다.'%findName)
    elif menu=='4' :
        # 학생 자료 삭제하기
        delName=input('삭제하려는 학생의 이름은?:')
        try :
            findIndex=name.index(delName)
            name.pop(findIndex)
            kor.pop(findIndex)
            eng.pop(findIndex)
            math.pop(findIndex)
        except ValueError :
            print('%s 우리반 학생이 아닙니다.'%delName)

    elif menu=='5' :
        # 프로그램 종료하기5
        a=10


''' 검색 프로그램 
findName=input('점수를 알고 싶은 학생 이름은?:')
            okName=-1      
            for i in range(len(name)) :
                if findName== name[i] :
                    okName=i
                    break
            if okName==-1 :
                print('%s는 우리 반 학생이 아닙니다.'%findName)
            else : 
                print('%s %d %d %d'%(name[okName],kor[okName],eng[okName],math[okName]))
'''