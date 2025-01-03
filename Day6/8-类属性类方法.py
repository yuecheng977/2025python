class Tool:
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    def __del__(self):
        Tool.count -= 1

    @classmethod
    def show_tool_count(cls):
        print(cls.count)

    @staticmethod
    def help():
        print("这是一个工具箱，作用是实例化各种工具对象")


tool1 = Tool('工具1')
tool2 = Tool('工具2')
print(Tool.count)
Tool.show_tool_count()
Tool.help()
