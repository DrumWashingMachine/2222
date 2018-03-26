pattern='abba'
str1='dog cat cat dog'
def re(pattern,str1):
    list1 = ','.join(pattern)
    list2 = list1.replace('a', 'dog')
    list3 = list2.replace('b', 'cat')
    list4=list3.replace(',',' ')
    print(list4)
    return list4==str1

print(re(pattern,str1))

