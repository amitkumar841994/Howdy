lst=[4,3,8,2,5]
target=9

my_dict = {}

for key,value in enumerate(lst):
    total = target - value
    if value in my_dict.keys():
        pass
    else:
        my_dict[value] = key
print(my_dict)