class Student:
    def __init__(self, name, student_id, age):
        self.name = name
        self.student_id = student_id
        self.age = age
    
    def display_info(self):
        print(f"姓名: {self.name}, 学号: {self.student_id}, 年龄: {self.age}")

student1 = Student("张三", "2023001", 20)
student2 = Student("李四", "2023002", 19)
student3 = Student("王五", "2023003", 21)

student1.display_info()
student2.display_info()
student3.display_info()

class ResearchDirection:
    def __init__(self, direction_name, field, description=""):
        self.direction_name = direction_name
        self.field = field
        self.description = description
    
    def display_info(self):
        print(f"研究方向: {self.direction_name}, 领域: {self.field}")
        if self.description:
            print(f"方向描述: {self.description}")

class Supervisor:
    def __init__(self, name, title, research_field, contact_info=""):
        self.name = name
        self.title = title
        self.research_field = research_field
        self.contact_info = contact_info
    
    def display_info(self):
        print(f"导师: {self.name}, 职称: {self.title}, 研究领域: {self.research_field}")
        if self.contact_info:
            print(f"联系方式: {self.contact_info}")

class Undergraduate(Student):
    def __init__(self, name, student_id, age, major, elective_courses=None):
        super().__init__(name, student_id, age)
        self.major = major
        self.elective_courses = elective_courses or []
    
    def add_course(self, course):
        self.elective_courses.append(course)
    
    def display_info(self):
        super().display_info()
        print(f"专业: {self.major}, 选修课程: {', '.join(self.elective_courses)}")

class Graduate(Student):
    def __init__(self, name, student_id, age, research_direction, supervisor, papers_count=0, research_progress=0):
        super().__init__(name, student_id, age)
        
        if isinstance(research_direction, ResearchDirection):
            self.research_direction = research_direction
        else:
            self.research_direction = ResearchDirection(research_direction, "未指定")
        
        if isinstance(supervisor, Supervisor):
            self.supervisor = supervisor
        else:
            self.supervisor = Supervisor(supervisor, "教授", "未指定")
        
        self.papers_count = papers_count
        self.research_progress = research_progress
    
    def update_research_progress(self, progress):
        self.research_progress = max(0, min(100, progress))
    
    def update_papers_count(self, count):
        self.papers_count = max(0, count)
    
    def add_paper(self):
        self.papers_count += 1
    
    def display_info(self):
        super().display_info()
        self.research_direction.display_info()
        self.supervisor.display_info()
        print(f"发表论文: {self.papers_count}篇, 研究进度: {self.research_progress}%")

if __name__ == "__main__":
    print("本科生测试")
    ug1 = Undergraduate("张三", "UG2023001", 20, "计算机科学")
    ug1.add_course("人工智能")
    ug1.add_course("数据结构")
    ug1.display_info()
    
    print("\n研究生测试")
    ml_direction = ResearchDirection("机器学习", "人工智能", "研究机器学习算法及其应用")
    
    prof_wang = Supervisor("王教授", "教授", "人工智能与机器学习", "wang@university.edu")
    
    g1 = Graduate("李四", "G2023001", 25, ml_direction, prof_wang, 3, 60)
    g1.display_info()
    
    print("\n研究生更新信息后")
    g1.update_research_progress(80)
    g1.add_paper()
    g1.display_info()
    