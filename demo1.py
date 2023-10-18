class Student:
    name = None
    age = None
    ad = None
    def __init__(self,name,age,ad):
        self.name = name
        self.age = age
        self.ad = ad
        print(f'【学生姓名：{name}，年龄：{age}，地址：{ad}】')

for i in range(1,11):
    print(f'当前录入第{i}位学生信息，总共需录入10位学生信息')
    name = input('请输入学生姓名：')
    age = int(input('请输入学生年龄：'))
    ad = input('请输入学生地址：')
    print(f'学生{i}信息录入完成，信息为：',end='')
    stu = Student(name,age,ad)
