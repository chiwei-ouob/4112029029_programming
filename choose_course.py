courses = [] #課程清單
class Course:
    student_list = [] 
    def __init__(self, title, course_id, time, professor): #課程屬性初始化
        self.title = title
        self.course_id = course_id
        self.time = time
        self.professor = professor
        
    def added_by_student(self, student_id): #將學生新增至課程的學生清單
        self.student_list.append(student_id)
        print("Successfully added student to the course.")
        
    def show_course_info(self): #輸出課程資料
        print(f"\n課程名稱: {self.title} \n課程代碼: {self.course_id}\n上課時間: {self.time}\n教授: {self.professor}\n學生清單: ")
        for student in self.student_list:
            student.show_student_info()
            
    def show_brief_course_info(self): #輸出課程資料
        print(f"課程名稱: {self.title} \n課程代碼: {self.course_id}\n上課時間: {self.time}\n教授: {self.professor}")

            
    def lookup_course(self, target_id): #函式lookup_courses的第二階段判斷，此課程是否存在
        if self.course_id == target_id:
            return True
        else:
            return False
            
        
students = [] #學生清單
class Student(Course):
    course_list = []
    def __init__(self, name, student_id): #學生屬性初始化 #完成
        self.name = name
        self.student_id = student_id
        
    def add_course(self, course_id): #將課程加入該生的選課清單中(也就是加選) 
        course = lookup_courses(course_id) #判斷課程是否存在
        if course!=False: #若課程存在
            self.course_list.append(course)
            print("成功加選! \n你目前已經選了: ")
            for course in self.course_list:
                    course.show_brief_course_info()
        else:
            print ("Wrong course id.")
            
    def cancel_course(self, course_id): #學生退選課程 
        course = self.lookup_own_courses(course_id) #判斷課程是否存在
        if course!=False: #若課程存在
            self.course_list.remove(course)
            print("成功退選! \n你目前已經選了: ")
            for course in self.course_list:
                    course.show_brief_course_info()
        else:
            print ("Wrong course id.")

    def show_student_info(self): #輸出學生資料 #已完成
        print(f"學生姓名: {self.name} \n學號: {self.student_id}\n選課清單: ")
        for course in self.course_list:
            course.show_course_info()
        
    def lookup_student(self, target_id): #函式lookup_students的第二階段判斷，此學生是否存在
        if self.student_id == target_id:
            return True
        else:
            return False
        
    def lookup_own_courses(self,course_id): #查詢學生是否有選這個課程
        for selected_data in self.course_list:
            outcome = selected_data.lookup_course(course_id)
            if outcome == True:
                return selected_data
                break
        return False
        
        
def lookup_courses(course_id): #查詢該代號是否有所指之課程，有則回傳課程(物件) #完成
    for selected_data in courses:
        outcome = selected_data.lookup_course(course_id)
        if outcome == True:
            return selected_data
            break
    return False
def lookup_students(student_id): #查詢該學號是否有所指之學生，有則回傳學生(物件) #完成
    for selected_data in students:
        outcome = selected_data.lookup_student(student_id)
        if outcome == True:
            return selected_data
            break
    return False
         

def add_courses(): #新增課程 #完成
    title = input("title: ")
    course_id = int(input("course_id (four number):"))
    time = input("time:")
    professor = input("professor:")
    if course_id >1000 and course_id <= 9999:
        course = Course(title, course_id, time, professor)
        courses.append(course) 
def add_students(): #新增學生 #完成
    name = input("name:")
    student_id = int(input("student_id:"))
    if student_id >4000000000 and student_id <= 4999999999:
        student = Student(name, student_id)
        students.append(student)

        
def choose_course(): #學生選課主選單
    user_student = int(input("Enter your student id: "))
    student = lookup_students(user_student)
    if  student != False:
        while True:
            option=input("學生選單\n1:加選 2:退選 3:登出")
            if option == "3": 
                print ("已登出!\n")
                break
            elif option == "1":
                print ("可選課程:")
                for course in courses:
                    course.show_brief_course_info()
                course_id = int (input("輸入課程代碼: ")) 
                student.add_course(course_id)
                
            elif option == "2":
                print ("目前已選課程:")
                for course in student.course_list:
                    course.show_brief_course_info()
                course_id = int (input("輸入課程代碼: ")) 
                student.cancel_course(course_id)
    else:
        print ("Wrong id.")
            
        
def main():
    while True:
        option=input("主選單\n1:新增課程資料 2:新增學生資料 3:學生選課")
        if option == "1":
            add_courses()
            for course in courses:
                course.show_course_info()
                
        elif option == "2":
            add_students()
            for student in students:
                student.show_student_info()
            
        elif option == "3":
            choose_course()

if __name__ == "__main__": #底線有兩個
    main()