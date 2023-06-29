def quick_sort(sort_list,pivot_element):
    if len(sort_list) in [0,1]:
        return sort_list
        
    finlist=quick_sort([i for i in sort_list if i<sort_list[pivot_element]],pivot_element)+[i for i in sort_list if i==sort_list[pivot_element]]+quick_sort([i for i in sort_list if i>sort_list[pivot_element]],pivot_element)

    return finlist


print("Enter list of integers seperated by commas to get a sorted list.")
L1=list(map(int,input().split(",")))

sortedlist=quick_sort(L1,-1)

print(sortedlist)