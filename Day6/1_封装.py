class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n 总面积：%.2f[剩余：%.2f]\n 家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item: HouseItem):
        if self.free_area > item.area:
            self.item_list.append(item.name)
            self.free_area -= item.area
        else:
            print("房子没空间了")
            return


if __name__ == '__main__':
    bed = HouseItem('席梦思', 4)
    chest = HouseItem('衣柜', 2)
    table = HouseItem('桌子', 2)
    print(bed, chest, table)
    my_home = House("两室一厅", 60)
    my_home.add_item(bed)
    my_home.add_item(chest)
    my_home.add_item(table)
    print(my_home)
