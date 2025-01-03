# while True:
#     try:
#         num= int(input('请输入一个整数'))
#         print(num)
#         break
#     except:
#         print('输入的数必须是整数')


def input_int_duicheng():
    #
    num = int(input("请输入整型数："))

    #
    if str(num) == str(num)[::-1]:
        return num
    raise Exception("不是回文数")


if __name__ == '__main__':
    try:
        print(input_int_duicheng())
    except ValueError:
        print("请输入整数")
    except Exception as result:
        print(result)
