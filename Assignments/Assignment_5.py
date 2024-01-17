name1 = 'Sanidhya Singla'
print(name1.split())
class1 = 8
section1 = 'D'
name2 = 'Gaurav SINGLA'
class2 = 8
section2 = 'D'
name3 = 'Nidhi singla'
class3 = 8
section3 = 'D'

list1 = [name1, class1, section1]
list2 = [name2, class2, section2]
list3 = [name3, class3, section3]

class_list = [list1, list2, list3]

name_list = []


def getnames(class_list):
    name_list1 = []
    for n in class_list:
        name_list1.append(n[0])
    return (name_list1)


def getsurnamecount(classlist):
    count = 0
    for n in classlist:
        if (n[0].split()[-1].lower() == 'singla'):
            count += 1
    return (count)


print('Class list:', class_list)
print('Name list:', name_list)

print(getnames(class_list))
print(getsurnamecount(class_list))
