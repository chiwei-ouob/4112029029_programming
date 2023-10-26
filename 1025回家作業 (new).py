# 1. 回傳兩字典中，共有的鍵之值總合
def SumKey(dict1, dict2):
    output_dict = {}
    for key1, value1 in dict1.items():
        for key2, value2 in dict2.items():
            if key1 == key2:
                output_dict[key1] = value1 + value2
    print(output_dict)
print("\n\n=====SUMMARY OF KEYS=====\n")
SumKey({'a': 5, 'b': 2, 'c': 3, 'd': 4}, {'a': 10, 'b': 3, 'e': 5, 'f': 7})

# 2. 回傳一字串中，各字元出現數量


def CountChar(string):
    output_dict = {}
    for char in string:  # 可優化: 使用 string.lower() 可以使大小寫字母視為相同小寫字母並一起累計
        if char in output_dict:  # 判斷該字元是否曾出現在字典(的鍵)
            output_dict[char] += 1
        else:
            output_dict[char] = 1
    print(output_dict)
print("\n\n=====COUNT EACH CHARACTERS=====\n")
CountChar("hello world")

# 3. 成績紀錄簿


def ScoreBook():
    class Student:
        def __init__(self, name):
            self.name = name
            self.grades = {}

    class Gradbook:
        def __init__(self):
            self.student_list = []

        def add_student(self, student):
            self.student_list.append(Student(student))

        def add_score(self, student, subject, score):
            for i in range(len(self.student_list)):
                if self.student_list[i].name == student:
                    self.student_list[i].grades[subject] = score
                # else: print ("Wrong name.")

        def average(self, subject):
            try:
                for student in self.student_list:
                    if subject not in student.grades:
                        raise Exception('成績有缺少')
                print(sum([i.grades[subject] for i in self.student_list]
                          )/len(self.student_list))  # 所有人都有該科成績才執行此行
            except Exception as e:
                print(e)  # 輸出錯誤訊息

  # 測試用主程式
    gradebook = Gradbook()
    print("\n\n=====GRADE BOOK=====\n")
    while True:
        choice = input("\n1. add student 2. add score 3. average 4. end: ")
        if choice == "1":
            name = input("Name: ")
            gradebook.add_student(name)
        elif choice == "2":
            name = input("Name: ")
            subject = input("Subject: ")
            score = int(input("Score: "))
            gradebook.add_score(name, subject, score)
        elif choice == "3":
            subject = input("Subject: ")
            gradebook.average(subject)
        elif choice == "4":
            break
        else:
            print("Again.")
    '''  # 測資
1
Amy
1
Ben
1
Cindy
2
Amy
Math
95
2
Amy
English
80
2
Ben
Math
65
2
Ben
English
75
2
Cindy
Math
70
3
Math
3
English
4

    '''


ScoreBook()


# 4. 員工管理系統


def EMS_function():  # EmployeeManagementSystem
    class Employee:
        def __init__(self, id, name):  # 所有員工初始化時，皆僅輸入其編號與名字
            self.id = id
            self.name = name

        def calculate_salary(self):
            pass  # 什麼都不做

    class FullTimeEmployee (Employee):  # 全職員工
        def __init__(self, id, name):
            super().__init__(id, name)
            self.salary = 0

        def calculate_salary(self):
            return self.salary

    class PartTimeEmployee (Employee):  # 兼職員工
        def __init__(self, id, name):
            super().__init__(id, name)
            self.hours_worked = 0
            self.hourly_wage = 0

        def calculate_salary(self):
            return self.hours_worked * self.hourly_wage

        def set_hours_worked(self, hours):
            self.hours_worked = hours

    class Intern (Employee):
        def __init__(self, id, name):
            super().__init__(id, name)
            self.stipend = 0

        def calculate_salary(self):
            return self.stipend

    class EmployeeManagementSystem:
        def __init__(self):
            self.employee_list = []
            self.id = 1

        def add_employee(self, employee):  # 為判斷員工類別，employee -> (name, position_code)
            if employee[1] == "1":  # full time
                self.employee_list.append(
                    FullTimeEmployee(self.id, employee[0]))
                print("Full time employee added.")
            elif employee[1] == "2":  # part time
                self.employee_list.append(
                    PartTimeEmployee(self.id, employee[0]))
                print("Part time employee added.")
            elif employee[1] == "3":  # intern
                self.employee_list.append(Intern(self.id, employee[0]))
                print("Intern employee added.")
            else:
                print("Position code error.")
            self.id += 1

        def calculate_all_salary(self):
            return sum([employee.calculate_salary() for employee in self.employee_list])

        def add_work_hours(self, employee, hours, wage):
            try:
                for i in range(self.id-1):
                    if self.employee_list[i].name == employee:
                        # 判斷物件是否具有該屬性(為避免值為0而被視為不存在，故+1)
                        assert hasattr(
                            self.employee_list[i], "hours_worked"), Exception("這位不是兼職員工")
                        self.employee_list[i].set_hours_worked(hours)
                        self.employee_list[i].hourly_wage = wage
                        print(
                            f"{self.employee_list[i].name} worked {hours} hours, and the wage per hour is {wage}.")
            except Exception as e:
                print(e)

        def set_stipend(self, employee, stipend):
            try:
                for i in range(self.id-1):
                    if self.employee_list[i].name == employee:
                        assert hasattr(
                            self.employee_list[i], "stipend"), Exception("這位不是實習生")
                        self.employee_list[i].stipend = stipend
                        print(
                            f"{self.employee_list[i].name}'s stipend is {stipend}.")
            except Exception as e:
                print(e)

        def set_full_time_salary(self, employee, salary):
            try:
                for i in range(self.id-1):
                    if self.employee_list[i].name == employee:
                        # hasattr(object, "attribute") -> check if object has attribute
                        assert hasattr(
                            self.employee_list[i], "salary"), Exception("這位不是全職員工")
                        self.employee_list[i].salary = salary
                        print(
                            f"{self.employee_list[i].name}'s salary is {salary}.")
            except Exception as e:
                print(e)

        def print_all_employee(self):
            for employee in self.employee_list:
                print(
                    f"{employee.name} (ID: {employee.id}): ${employee.calculate_salary()}")

        def print_employee(self, employee):
            for staff in self.employee_list:
                if staff.name == employee:
                    print(
                        f"{staff.name} (ID: {staff.id}): ${staff.calculate_salary()}")
                    break
            else:
                print("Employee not found.")  # 此行只有當"for迴圈未執行break時"才會執行

    # 測試用主程式
    EMS = EmployeeManagementSystem()
    print("\n\n=====EMPLOYEE MANAGEMENT SYSTEM=====\n")
    while True:
        choice = input(
            "\n1. add employee 2. update employee\'s info 3. calculation 4. end: ")
        if choice == "1":
            while True:
                name = input(
                    "\nEmployee\'s name (\"back\" for accessing main menu): ")
                if name.lower() == "back":
                    break
                position = input(
                    "Identity (1. full time 2. part time 3. intern): ")
                if position in ['1', '2', '3']:
                    EMS.add_employee((name, position))
                else:
                    print("Wrong position.")
        elif choice == "2":
            while True:
                name = input(
                    "\nEmployee\'s name (\"back\" for accessing main menu): ")
                if name.lower() == "back":
                    break
                position = input(
                    "Identity (1. full time 2. part time 3. intern): ")
                if position == "1":
                    try:
                        salary = int(input("Salary: "))
                        assert salary > 0, Exception(
                            "Salary should be more than zero.")
                        EMS.set_full_time_salary(name, salary)
                    except Exception as e:
                        print(e)
                elif position == "2":
                    try:
                        hour = int(input("Work hour: "))
                        assert hour > 0, Exception(
                            "Work time should be more than zero hour.")
                        wage = int(input("Wage per hour: "))
                        assert wage > 0, Exception(
                            "Wage per hour should be more than zero.")
                        EMS.add_work_hours(name, hour, wage)
                    except Exception as e:
                        print(e)
                elif position == "3":
                    try:
                        stipend = int(input("Stipend: "))
                        assert stipend > 0, Exception(
                            "Stipend should be more than zero.")
                        EMS.set_stipend(name, stipend)
                    except Exception as e:
                        print(e)
                else:
                    print("Again.")
        elif choice == "3":
            while True:
                select = input(
                    "\n1. all salary 2. each employees\' salaries 3. certain employee\'s salary  (\"back\" for accessing main menu): ")
                if select.lower() == "back":
                    break
                elif select == "1":
                    print("\n====== All salary ======")
                    print(
                        f"All salaries and wages: ${EMS.calculate_all_salary()}")
                elif select == "2":
                    print("\n====== Each employees\' salaries ======")
                    EMS.print_all_employee()
                elif select == "3":
                    name = input("Employee's name: ")
                    EMS.print_employee(name)
        elif choice == "4":
            break
        else:
            print("Again.")
    '''  # 測資
1
Amy
1
Ben
2
Cindy
3
back
2
Amy
1
-1
Amy
1
15000
Ben
2
0
Ben
2
10
180
Cindy
1
10000
Cindy
3
10000
Amy
1
15500
back
3
1
2
3
Amy
3
Ben
3
Cindy
3
Matt
back
5
4
    '''


EMS_function()
