lst=[9,9,9]
a=''
lst2=[]
for i in lst:
    a=str(i)+a
b=int(a[::-1]) + 1
c=str(b)
print(c)
for char in c:
    lst2.append(int(char))

print(lst2)

# for i in b:
#     list(lst2).append(i)
# print(lst2)
