#該如何讀取xml檔案
import xml.etree.ElementTree as ET
#匯入函數庫
def compound_interest(x,s,y):
    total = 0 #計算複利的總和
    for i in range(y):#總共y年
        total = (total + x)#經過複利的金額+新投資的金額
        total = total*(1+s/100)#複利
    return total
# 解析XML文件

tree = ET.parse("setting.xml")# 讀取setting.xml的檔案
root = tree.getroot()# 建立樹結構
# 如何把這樹結構轉化成python可以使用的資料?
# 创建一个空字典:在python裡類似樹結構的東西都是用{}做建立

data_dict = {}# data ={key : value}
# 遍历XML元素并将其存储在字典中
for element in root:
    key = element.tag  # 讀取tag : x,s,y
    value = element.text  # 把資料存到python裡的字典處理
    data_dict[key] = value
# 打印字典
print(data_dict)
x = int(data_dict['x'])
s = int(data_dict['s'])
y = int(data_dict['y'])
# x = int(input("每年投資的金額"))
# s = int(input("年利率"))
# y = int(input("年份"))

print(compound_interest(x,s,y))
# 不但要存計算出結果且要存至記事本
# 打開記事本檔案
file = open("result.txt","w",encoding = "utf-8")
# "result.txt" -> 檔案名稱
# "w" ->write寫人
# encoding -> 文字編碼 繁體用的是"utf-8" 簡體"big-5"
file.write("本金:"+str(x)+"\n")
file.write("年利率:"+str(s)+"\n")
file.write("投資年分:"+str(y)+"\n")
file.write("------以下是您可以得到的總金額------\n")
#file.write(str(int(compound_interest(x,s,y)))+".00元")
num = compound_interest(x,s,y)
file.write(f"{num:.2f}元")#字串格式化
file.close()