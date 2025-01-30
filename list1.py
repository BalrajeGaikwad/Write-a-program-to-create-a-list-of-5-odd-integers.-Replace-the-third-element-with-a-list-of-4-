"""
Write a program to create a list of 5 odd integers. Replace the third element with a list of 4 even integers. Flatten, sort and print the list.

"""



odd=[1,3,5,7,9]

even=[2,4,6,8]

odd[2]=even

flatten_list=[]
for item in odd:
    if isinstance(item, list):
        flatten_list.extend(item)
    else:
        flatten_list.append(item)

flatten_list.sort()

print(flatten_list)