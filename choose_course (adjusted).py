courses = [] #課程清單
class Course:
     #所存之學生資訊，其"已選課程"可能有誤，但不影響程式執行
    def __init__(self, title, course_id, time, professor): #課程屬性初始化
        self.title = title
        self.course_id = course_id
        self.time = time
        self.professor = professor
        self.student_list = []
        
    def added_by_student(self, student): #將學生新增至課程的學生清單
        if student not in self.student_list:
            self.student_list.append(student)
            print("成功將你加入該課程中。")

    def removed_by_student(self, student): #將學生移除自課程的學生清單
        self.student_list.remove(student)
        print("成功將你移出該課程中。")
        
    def show_course_info(self): #輸出課程資料
        print(f"\n課程名稱: {self.title} \n課程代碼: {self.course_id}\n上課時間: {self.time}\n教授: {self.professor}\n學生清單: ")
        for student in self.student_list:
            student.show_brief_student_info()
        if len(self.student_list)==0:
            print ("尚無學生。")
            
    def show_brief_course_info(self): #輸出課程資料
        print(f"課程名稱: {self.title} ({self.course_id})\n上課時間: {self.time}\n教授: {self.professor}\n")

            
    def lookup_course(self, target_id): #函式lookup_courses的第二階段判斷，此課程是否存在
        if self.course_id == target_id:
            return True
        else:
            return False
            
        
students = [] #學生清單
class Student(Course):
    
    def __init__(self, name, student_id): #學生屬性初始化 #完成
        self.name = name
        self.student_id = student_id
        self.course_list = []
        
    def add_course(self, course): #學生加選課程 
            self.course_list.append(course)
            print("成功加選! \n你目前已經選了: ")
            for course in self.course_list:
                course.show_brief_course_info()
            
    def cancel_course(self, course): #學生退選課程 
        self.course_list.remove(course)
        print("成功退選! \n你目前已經選了: ")
        for course in self.course_list:
                course.show_brief_course_info()

    def show_student_info(self): #輸出學生資料 #已完成
        print(f"學生姓名: {self.name} \n學號: {self.student_id}\n選課清單: ")
        for course in self.course_list:
                course.show_brief_course_info()
        if len(self.course_list)==0:
            print("尚無課程。")
                
    def show_brief_student_info(self):
        print(f"學生姓名: {self.name} 學號: {self.student_id}")
        
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
    title = input("課程名稱: ")
    course_id = int(input("課程代碼(四位數):"))
    time = input("上課時間:")
    professor = input("授課教授:")
    if course_id >1000 and course_id <= 9999:
        course = Course(title, course_id, time, professor)
        courses.append(course) 
    else: 
        print ("課程代碼無效。")
def add_students(): #新增學生 #完成
    name = input("學生姓名:")
    student_id = int(input("學生學號:"))
    if student_id >4000000000 and student_id <= 4999999999:
        student = Student(name, student_id)
        students.append(student)

        
def choose_course(): #學生選課主選單
    user_student = int(input("輸入你的學號: "))
    student = lookup_students(user_student)
    if  student != False:
        while True:
            option=input(f"\n學生選單\n{student.name}，你好\n1:加選 2:退選 3: 查看目前選課狀態 4:登出")
            if option == "4": 
                user_student = 0
                print ("已登出!\n")
                break

            elif option == "1":
                print ("可選課程:")
                for course in courses:
                    course.show_brief_course_info()
                course_id = int (input("輸入課程代碼: ")) 
                course = lookup_courses(course_id)
                if course != False and course not in student.course_list:
                    course.added_by_student(student)
                    student.add_course(course)
                elif course in student.course_list:
                    print ("請勿重複選課。")
                else:
                    print("課程代碼無效。")

            elif option == "2":
                print ("目前已選課程:")
                for course in student.course_list:
                    course.show_brief_course_info()
                course_id = int (input("輸入課程代碼: "))
                course = lookup_courses(course_id)
                if course != False:
                    course.removed_by_student(student)
                    student.cancel_course(course)
                else:
                    print("課程代碼無效。")

            elif option == "3":
                student.show_student_info()
                
    else:
        print ("學號無效。")
            
        
def main():
    while True:
        option=input("\n主選單\n1:新增課程資料 2:新增學生資料 3:學生選課 4: 顯示課程資訊 5:離開")
        if option == "1":
            add_courses()
            # for course in courses:
            #     course.show_course_info() #測試顯示所有課程
                
        elif option == "2":
            add_students()
            # for student in students:
            #     student.show_student_info() #測試顯示所有學生
            
        elif option == "3":
            choose_course()
            
        elif option == "4":
            target_id = int(input("輸入欲查詢之課程代碼: "))
            course = lookup_courses(target_id)
            if course != False:
                course.show_course_info()
            else:
                print ("代碼無效。")

        elif option == "5":
            break
        
        elif option == "6":
            for student in students:
                student.show_student_info() #測試顯示所有學生




if __name__ == "__main__": #底線有兩個
    main()