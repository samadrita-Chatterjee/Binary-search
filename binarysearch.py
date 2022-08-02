def binary_search(my_list,num):
    low=0
    upp= len(my_list) - 1
    mid=0
    while low <= upp:
        mid=(upp + low) // 2
        if my_list[mid] < num:
            low = mid + 1
        elif my_list[mid] > num:
            upp= mid - 1
        else:
            return mid
    return -1
num=int(input("Enter a number to search: "))
my_list=[4,5,10,12,18,23,40,55,56,80]
result = binary_search(my_list,num)
if result != -1:
    print("Number  Found at index", str(result))
else:
    print("Number not found in the list")