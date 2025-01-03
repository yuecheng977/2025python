class Person:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    p1 = Person('Jay')
    p2 = Person('David')
    print(p1.name)
    print(p2.name)
    print(p1 is p2)
