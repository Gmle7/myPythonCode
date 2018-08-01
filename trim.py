def trim(word):#去除字符串首尾的空格
    if word=='':
        return word
    elif word[0]==' ':
        return trim(word[1:])
    elif word[-1]==' ':
        return trim(word[:-1])
    else:
        return word

print(trim('  he llo '))

def trim2(word):#去除字符串的空格
    list1=''
    list2=[]
    for i,value in enumerate(word):
        if value!=' ':
            list1=list1+value
            list2.append(value)
    print(list1)
    print(list2)
trim2('  h e ll o ')

def findMinAndMax(L):
    if len(L)==0:
        return (None,None)
    else:
        min=max=L[0]
        for l in L:
            if l>max:
                max=l
            elif l<min:
                min=l
    return (min,max)

findMinAndMax([1,5744,484])
# def show():
#     if findMinAndMax([]) != (None, None):
#         print('测试失败!')
#     elif findMinAndMax([7]) != (7, 7):
#         print('测试失败!')
#     elif findMinAndMax([7, 1]) != (1, 7):
#         print('测试失败!')
#     elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#         print('测试失败!')
#     else:
#         print('测试成功!')

# show()