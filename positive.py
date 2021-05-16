mylist=[]
len=int(input("enter number of elements: "))
for i in range(0, len):
    value=int(input())
    mylist.append(value)
num=list(filter(lambda i:(i>=0), mylist))
print(" the positive number are: ", num)
for ele in mylist:
    if ele>=0:
        print(ele, end=",")
