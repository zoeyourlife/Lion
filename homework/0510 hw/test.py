# score = float(input("내 점수는? ")) #실수형으로 성적 입력

# if score >= 80:
#     print("A")
# elif score>=60 and score<80:
#     print("B")
# elif score>=40 and score<60:
#     print("C")
# elif score<40:
#     print("D")
    

# for 변수 in range(시작값, 끝값+1, 증가 값):
# 반복할 문장
# i = 0
# while i<3:
#     print("나는야 아기사자")
#     i = i+2


#과제...!
lion = int(input("숫자를 입력해주세요: "))
i = 0
if(lion<10):
    while i<lion:
        print("멋쟁이")
        i+=1
elif(lion>=10):
    print("사자처럼")