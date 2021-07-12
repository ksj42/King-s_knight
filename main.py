#현재 나이트 위치 입력받기
input_data=input()                              #문자데이터
#print(input_data[0])                            #그냥 그대로
#print(ord(input_data[0]))                       #ord하면 앞문자를 아스키 변환
#print(ord('a'))                                 #'a'문자의 아스키값 '97' 출력
#print(row)
#print(colum)
row=int(input_data[1])                          #두번째 문자는 행의 정보이므로 row에저장
colum=int(ord(input_data[0]))-int(ord('a'))+1   #첫번째 문자는 열의 정보이고 숫자문자이므로

#나이트가 이동할 수있는 8가지 방향 정의
steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)] #파이썬은 리스트가 배열이다

#8가지 방향에 대하여 가 ㄱ위치로 이동이 가능한지 확인
result=0
for step in steps:
    #이동하고자 하는 위치 확인
    next_row=row+step[0]
    next_colum=colum+step[1]
    if next_row>=1 and next_row<=8 and next_colum>=1 and next_colum<=8 :
        result+=1
print(result)

