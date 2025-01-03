class Dog:
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)


class XiaoTianQuan(Dog):

    def game(self):
        print("%s 飞到天上去玩耍..." % self.name)

class Person:
    def __init__(self,name):
        self.name = name

    def game_with_dog(self,dog:Dog):
        print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))
        dog.game()


if __name__ == '__main__':
    zhangsan = Person("zhangsan")
    wangcai = Dog('wangcai')
    zhangsan.game_with_dog(wangcai)
    xiaotianquan=XiaoTianQuan('xiaotianquan')
    zhangsan.game_with_dog(xiaotianquan)