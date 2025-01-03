class Women:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __secret(self):
        print(f'{self.name}年龄{self.__age}')

    def boy_friend(self):
        self.__secret()


if __name__ == '__main__':
    xiaohong = Women('小红', 18)
    xiaohong.boy_friend()
