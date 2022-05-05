import random
import time

lunch = ["냉면", "고기", "떡"]

while True:
    print(lunch)
    item = input("메뉴를 추가해 주세요: ")
    if(item == "q"):
        break
    else:
        lunch.append(item)

set_lunch = set(lunch)

while True:
    print(set_lunch)
    item = input("메뉴를 삭제해 주세요: ")
    if(item == "q"):
        break
    else:
        set_lunch = set_lunch - set([item])

print(set_lunch, "중에서 뽑습니다.")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print(random.choice(list(set_lunch)))