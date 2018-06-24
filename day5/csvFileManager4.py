import csv
import os


class CsvFileManager4:
    def read(self,file_path):
        list=[]
        base_path=os.path.dirname(__file__)
        # print(base_path)
        path=base_path.replace("day5","data/"+file_path)
        # print(path)
        # file=open(path,'r')
        #每次打开文件，用完之后要记得关闭
        #我们上节课用的是try ..finally,更长用的方法是with ..as..
        with open(path,'r') as file:
            data_table=csv.reader(file)
            for row in data_table:
                list.append(row)
                # print(row)
                #打印出来不是我们的目的，我们的测试用例需要调用这个数据，所以，要给给ige返回值
               # 5，声明一个二维列表，保存到data_table
        return list
        #一个csv文件只适合

       # 2,指定CSV文件路径
        #path=r"C:\Users\cheng\PycharmProjects\selenium7th\data\tets_data.csv"
if __name__=="__main__":
    list=CsvFileManager4().read("test_data1.csv")
    print(list)