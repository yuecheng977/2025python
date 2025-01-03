class Parent:
    def __init__(self, name):
        self.name = name


class Son1(Parent):
    def __init__(self, age, *args):
        self.age = age
        super().__init__(*args)


class Son2(Parent):
    def __init__(self, score, *args):
        self.score = score
        super().__init__(*args)


class Grandson(Son1, Son2):
    def __init__(self, *args,height):
        self.height = height
        super().__init__(*args)


if __name__ == '__main__':
    xiaoming = Grandson(18, 98.5, '小明', height=175)  # 姓名，年龄，分数,身高
    print(xiaoming.name)
    print(xiaoming.age)
    print(xiaoming.score)
    print(xiaoming.height)
    print(Grandson.__mro__)
