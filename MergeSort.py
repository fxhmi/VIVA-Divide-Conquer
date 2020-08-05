
def lists(left_list, right_list):
    i = 0
    j = 0
    final_merge = []

    #iterate through left and right list
    while i < len(left_list) and j < len(right_list):  # if left value is lower than right then append it to result
        if left_list[i] <= right_list[j]:
            final_merge.append(left_list[i])
            i += 1
            # print(F' left :', final_merge )

        else: #if right value is lower than left than append it to final merge array
            final_merge.append(right_list[j])
            j += 1
            # print(F' right :', final_merge )

    #concatenate the rest of the left and right using subarray
    final_merge += left_list[i:] #select elements from i to end
    final_merge += right_list[j:] #select elements from j to end
    print(F' entah :', final_merge )

    #return the result
    return final_merge

def merge_sort(list):
    #if list contains only 1 element return it
    if len(list) <= 1: #base case
            return list
    else:
            #split the list into 2 list and iterately split it
            mid = int(len(list)/2)
            left_list = merge_sort(list[:mid]) #add the list from start to mid
            right_list = merge_sort(list[mid:]) # add the list from mid to end


            # print(F'haa', left_list)
            # print(F'hoo', right_list)
            return lists(left_list,right_list)



#test run
lab3_list = [84,23,62,44,16,30,95,51]

# for x in range(len(lab3_list)):
print(F'Lab 3 unsorted list : ' , lab3_list)
print(F'Lab 3 sorted list : ', merge_sort(lab3_list))

