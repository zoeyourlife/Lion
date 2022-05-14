#2 딕셔너리 명은 Dic인 빈 딕셔너리를 생성
Dic={}

#3 While True: 반복문을 이용해 정수인 key값과 문자열인 value 값을 입력받아
#  각각 key, value 변수에 저장해준 후, 이를 딕셔너리에 각각 key 값과 value 값으로 넣기

while True:
    key = input("key 입력: ")
    value = input("value 입력: ")
    
    if key == "0" or value == "문자열 종료":
        print("그만")
        print(Dic)
        break
    else:
        Dic[key] = value
    
    # if "0" in key or value =="문자열 종료":
    #     print("그만")
    #     print(Dic)
    #     break
    # else:
    #     Dic[key]=value

print("dict_keys: ", list(Dic.keys()))
print("dict_values: ", list(Dic.values()))
print(Dic.items())
    

#4 반복문 안에 조건문을 통해서
#  key 값에 정수 0이 입력된 경우 혹은 value에 문자열 종료가 입력된 경우
#  print()문을 통해 그만과 print()문을 이용해 딕셔너리를 출력하고
#  break를 통해 반복문 빠져나오기


#5 dict_keys 객체와 dict_values 객체, dict_items 객체를 리스트로 변환하여
#  각각 print()문을 이용해 출력