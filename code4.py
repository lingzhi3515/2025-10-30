students = {
    '001': {
        '姓名': '张三',
        '年龄': 21,
        '性别': '男',
        '成绩': {
            'python': 88,
            '数据结构': 85,
            '机器学习': 92,
            '数据库': 88
        }
    },
    '002': {
        '姓名': '李四',
        '年龄': 20,
        '性别': '女',
        '成绩': {
            'python': 78,
            '数据结构': 76,
            '机器学习': 80,
            '数据库': 74
        }
    },
    '003': {
        '姓名': '王五',
        '年龄': 22,
        '性别': '男',
        '成绩': {
            'python': 65,
            '数据结构': 72,
            '机器学习': 58,
            '数据库': 68
        }
    }
}

print("1. 初始学生信息字典:")
print(students)
print()

students['004'] = {
    '姓名': '赵六',
    '年龄': 19,
    '性别': '女',
    '成绩': {
        'python': 90,
        '数据结构': 87,
        '机器学习': 85,
        '数据库': 91
    }
}

print("2. 添加004同学后的字典:")
print(students)
print()

students['001']['成绩']['数据结构'] = 88
print("3. 修改001同学数据结构成绩为88后:")
print(f"001同学的数据结构成绩: {students['001']['成绩']['数据结构']}")
print()

print("4. 两种方法访问001同学信息:")

print("方法1 - 直接键访问:")
print(f"姓名: {students['001']['姓名']}")
print(f"年龄: {students['001']['年龄']}")
print(f"性别: {students['001']['性别']}")
print(f"成绩: {students['001']['成绩']}")

print("\n方法2 - get()方法访问:")
print(f"姓名: {students.get('001', {}).get('姓名')}")
print(f"年龄: {students.get('001', {}).get('年龄')}")
print(f"性别: {students.get('001', {}).get('性别')}")
print(f"成绩: {students.get('001', {}).get('成绩')}")
print()

# 5. 遍历字典，打印所有同学的信息
print("5. 所有同学信息:")
print(f"{'学号'} {'姓名'} {'年龄'} {'性别'} {'Python'} {'数据结构'} {'机器学习'} {'数据库'}")


for student_id, info in students.items():
    grades = info['成绩']
    print(f"{student_id} {info['姓名']} {info['年龄']} {info['性别']} "
          f"{grades['python']} {grades['数据结构']} {grades['机器学习']} {grades['数据库']}")

for student_id, info in students.items():
    grades = info['成绩']
    scores = list(grades.values())
    avg_score = sum(scores) / len(scores)
    fail_count = sum(1 for score in scores if score < 60)
    
    if avg_score >= 85 and all(score >= 70 for score in scores):
        info['等级'] = '优秀'
    elif avg_score >= 75 and all(score >= 60 for score in scores):
        info['等级'] = '良好'
    elif avg_score >= 60 and fail_count <= 1:
        info['等级'] = '中等'
    elif avg_score >= 60:
        info['等级'] = '及格'
    else:
        info['等级'] = '不及格'


print("添加等级后的学生信息:")

print(f"{'学号'} {'姓名'} {'年龄'} {'等级'} {'Python'} {'数据结构'} {'机器学习'} {'数据库'}")


for student_id, info in students.items():
    grades = info['成绩']
    avg_score = sum(grades.values()) / len(grades)
    print(f"{student_id} {info['姓名']} {info['年龄']} {info['等级']} "
          f"{grades['python']} {grades['数据结构']} {grades['机器学习']} {grades['数据库']} ")
    
text = """Programming is the art of telling another human what one wants the computer to do Programming is a creative process that involves problem solving and logical thinking When we write code we are not just giving commands to a machine we are expressing ideas and solutions in a language that both humans and computers can understandThe joy of programming comes from the satisfaction of solving complex problems and creating something useful from nothing It is like building with digital bricks where each line of code contributes to the final structure Programmers experience a unique sense of accomplishment when their code runs successfully and produces the desired results"""

def count_word_frequency(text):
    words = text.lower().split()
    word_freq = {}
    for word in words:
        if word:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    return word_freq

word_freq = count_word_frequency(text)

print("原始词频统计:")
print(word_freq)
print()

print("1. 按字母排序:")
for word, freq in sorted(word_freq.items()):
    print(f"{word}: {freq}")

print("\n2. 按频率排序:")
for word, freq in sorted(word_freq.items(), key=lambda x: -x[1]):
    print(f"{word}: {freq}")

print("\n3. 按长度排序:")
for word, freq in sorted(word_freq.items(), key=lambda x: len(x[0])):
    print(f"{word}: {freq}")