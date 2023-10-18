class Atm:
    name = None
    money = None
    # opt = None

    def __init__(self,name,money):
        self.name = name
        self.money = money

    def menu(self):
        print('-----------主菜单-------------')
        print(f'{self.name}，您好，欢迎来到ATM，请选择操作：')
        print('查询余额\t[输入1]')
        print('存款\t[输入2]')
        print('取款\t[输入3]')
        print('退出\t[输入4]')
        opt = input('请输入您的选择：')
        return opt

    def yue(self):
        print(f'{self.name}，您好，您的余额剩余：{self.money}元')

    def cunkuan(self):
        print('-----------存款-------------')
        print(f'{self.name}，您好，', end='')
        num = int(input('请输入您的存款数字:'))
        self.money += num
        print(f'{self.name}，您好，您存款{num}元成功')
        self.yue()

    def qukuan(self):
        print('-----------取款-------------')
        print(f'{self.name}，您好，', end='')
        num = int(input('请输入您的取款数字:'))
        if self.money > num:
            self.money -= num
            print(f'{self.name}，您好，您取款{num}元成功')
            self.yue()
        else:
            print(f'{self.name}，您好，您取款{num}元失败，余额不足，请充值')

name = input('请输入您的姓名：')
heima = Atm(name,5000000)
while True:
    opt = heima.menu()
    if opt=='1':
        print('-----------查询余额-------------')
        heima.yue()
    elif opt=='2':
        heima.cunkuan()
    elif opt=='3':
        heima.qukuan()
    elif opt=='4':
        print('感谢您的使用，再会')
        break
    else:
        print('您输入的信息有误，请重新输入')