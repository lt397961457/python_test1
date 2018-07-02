# -*- coding: utf-8 -*-
name_list=["alex","steven","eric"]
name_list2=list(["alex2","steven2","eric2"])
print(name_list)
num = name_list.index("steven")
print(num)

name_list.insert(5,"ffff")
name_list.insert(len(name_list),"jjj")
name_list.remove("alex")
print(name_list)
print(name_list.pop(1))
print(name_list)
print(name_list2)

# 元祖,不可变列表
print("===========================")
ages=(11,22,33,44)
ages2=tuple((11,22,333,444))
print(ages)
print(ages2)