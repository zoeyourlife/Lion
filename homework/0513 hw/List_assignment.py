#2 리스트 명은 List인 빈 리스트 생성
List=[]

#3 첫번째 반복문. range() 1~15, 리스트의 요소로 추가, 조건문 15번째면 print()
for x in range(1,16): #1~15까지의 숫자를 포함하는 range 객체를 만든다.
    num = int(input())
    List.append(num)
    if(x==15):
        print(List)

# for x in range(20,35):
#     num = int(input())
#     List.append(num)
#     if(x==34):
#         print(List)

#4 두번째 반복문, 정수가 2의 배수라면 리스트에서 제거
for x in List:
    if(x%2==0):
        List.remove(x)

#5 리스트를 print()문을 사용해 출력
print(List)

#6 세번째 반복문 사용, 정수가 3의 배수라면 리스트에서 제거
for x in List:
    if(x%3==0):
        List.remove(x)

#7 리스트를 print()문을 사용해 출력
print(List)

#8 현재까지 리스트에 있는 요소는 1,5,7,11,13 이어야 한다.
# 이 리스트를 소수 리스트로 만들기 위해
# 1은 pop 함수와 print()문을 사용해 리스트에서 끄집어내주고
List.pop(0)
print(List)

# 2와 3은 insert 함수를 통해 삽입
# 인덱스 번호로 insert 하고싶은곳에 삽입.
List.insert(0,2)
List.insert(1,3)
print(List)
# 리스트 요소의 순서가 2,3,5,7,11,13 이 아니라면 sort함수 사용!