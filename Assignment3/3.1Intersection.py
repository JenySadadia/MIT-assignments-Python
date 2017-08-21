def list_intersection(list1,list2):
    list3=[]
    for i in list1:
        if(i in list2):
            list3.append(i)
    return list3

print(list_intersection([1,2,3],[2,4,3]))
