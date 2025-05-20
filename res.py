import os
import re

patten = re.compile(r"OnOnline_RequestMakeOnlineGuidance")   #编译筛选关键字
try:
    with open('C:/Users/18047/Desktop/delt.txt','r',encoding='utf-8',errors='replace') as file:  #打开log
        for i in file:
                if patten.search(i):   #搜索log中是否包含关键字
                    with open('C:/Users/18047/Desktop/1.txt', 'a', encoding='utf-8') as new:   #创建新文档
                        new.write(i)   #存入筛选后log
except FileNotFoundError as a:   #文件不存在抛出异常
    print(f"Not found file:{a}")
except Exception as e:      #抛出其他异常
    print(f"An error occurred: {str(e)}")
finally:
    with open ('C:/Users/18047/Desktop/1.txt','r',encoding='utf-8') as fi:
        f = fi.read()
        if len(f.strip()) ==0:      #判断是否为空
            print(f"not find {patten}")    #抛出搜索不到内容异常
        fi.close()













