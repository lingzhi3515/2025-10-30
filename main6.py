print("方式1: 导入整个模块")
import code6

# 使用模块名访问类
ug1 = code6.Undergraduate("张三", "UG2023001", 20, "计算机科学")
ug1.add_course("人工智能")
ug1.add_course("数据结构")
ug1.display_info()

print("方式2: 导入特定类")
from code6 import Graduate, ResearchDirection, Supervisor

ml_direction = ResearchDirection("深度学习", "人工智能", "研究深度神经网络")
professer_wang = Supervisor("王教授", "教授", "深度学习", "wang@university.edu")
g1 = Graduate("李四", "G2023001", 25, ml_direction, professer_wang, 3, 60)
g1.display_info()