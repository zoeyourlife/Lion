class Student: #파이썬에서 클래스란 객체를 찍어내는 틀
    # __init__을 사용하면 이 메소드는 생성자가 되고,
    # 객체를 만들며 동시에 실행되기 때문에 객체를 만들 때 가장먼저 초기화를 자동으로 시켜주는 메소드
    def __init__(self, name, grade, student_number, sex, address, phone_number, year):
        # 첫번째 매개변수 self는 메소드를 호출한 객체가 자동으로 전달된다.
        # 즉 self 매개변수에 해당 인스턴스를 받아오기 때문이고,
        # 사용할 때는 self를 제외한 값을 넘겨준다
        # 객체를 호출할 때 호출한 객체 자신이 전달되기 때문에 매개변수 이름은 self를 사용.
        self.name = name
        self.grade = grade
        self.student_number = student_number
        self.sex = sex
        self.address = address
        self.phone_number = phone_number
        self.year = year
        #self.x <-- 인스턴트 변수를 생성.
        
        #메소드 명 introduce. 이 메소드는 내가 원하는 출력들을 해줄 메소드이다.
    def introduce(self):
        print("이름은 %s이다." %self.name)
        print("학년은 %d이다" %self.grade)
        print("학번은 %d이다." %self.student_number)
        print("성별은 %s이다" %self.sex)
        print("주소는 %s이다." %self.address)
        print("전화번호는 %s이다." %self.phone_number)
        if self.year == "1": #self.year == "1" < input은 str형이므로 ""로 str형으로 인식하게 해준다.
            print("멋사 %s년차\n우와 아기사자다!" %self.year)
        else:
            print("멋사 %s년차\n우와 운영진이다!" %self.year)

#반복문 부분
while True:
    Class_name = input("객체 명을 입력하시오.(단, 영문으로): ") #객체명을 입력받고
    if Class_name == "종료": #입력받은 값이 종료라면 반복문 종료
        break
    # 쭉 매개변수값을 입력을 받고, 그 값들을 변수에 저장해준다.
    name = input("이름을 입력하시오.(단, 한글로): ")
    
    grade = int(input("학년을 입력하시오.(단, 숫자로): "))
    
    student_number = int(input("학번을 입력하시오.(단, 숫자로): "))
    
    sex = input("성별을 입력하시오.(모를 때는 모른다 라고 입력): ")
    if(sex == "모른다"):
        sex = "None"
        
    address = input("주소를 입력하시오.(~시까지만): ")
    
    phone_number = input("전화번호를 입력하시오(모를 때는 모른다 라고 입력.): ")
    if phone_number == "모른다":
        phone_number = "None"
        
    year = input("멋사 몇년차인가요?(단, 숫자로): ")
    
    #그 후 입력받은 객체명으로 Student 클래스를 하나 만들면서 그 안에 인스턴스 변수로
    # 입력받은 매개변수들을 저장해준다.
    Class_name = Student(name, grade, student_number, sex, address, phone_number, year)
    # 입력을 다 받으면 개행
    print("\n")
    #그 후 그 객체.메소드이름를 활용해 메소드를 사용(출력) 해준다.
    Class_name.introduce()
    
    # 그 후 다시 반복문으로 돌아가서 새로운 객체의 이름을 받고 매개변수값을 다시 받고
    # 새로운 객체의 이름으로 클래스를 생성해서 그 클래스의 인스턴스 변수에 매개변수 값들을
    # 다시 저장시켜주고 출력해준다.(반복)
    
    
    