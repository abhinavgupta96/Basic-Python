def bubble_sort(list_of_numbers):
    for i in range(0, len(list_of_numbers)) :
        for j in range(i+1, len(list_of_numbers)):
            ##since we have to compare with the next element
            if list_of_numbers[i] > list_of_numbers[j]:
                temp = list_of_numbers[i]
                list_of_numbers[i] = list_of_numbers[j]
                list_of_numbers[j] = temp
    return list_of_numbers


def selection_sort(list_of_numbers):
    for i in range(0, len(list_of_numbers)-1):
        minimum_index = i
        ##this value is set again and again for every item in the list that is smaller
        ## than the value at index i
        for j in range(i+1, len(list_of_numbers)):
            if list_of_numbers[j] < list_of_numbers[minimum_index]:
                minimum_index = j
        if i !=minimum_index:
            ## this is added to prevent swapping in the scenario where 
            ## the value being looked at is already the minimum unsorted value in the list
            temp = list_of_numbers[i]
            list_of_numbers[i] = list_of_numbers[minimum_index]
            list_of_numbers[minimum_index] = temp
    return list_of_numbers

def insertion_sort(list_of_numbers):
    for i in range(1,len(list_of_numbers)):
        temp = list_of_numbers[i]
        ##as insertion sort compares with item before the selected item, in this case 'i'
        j = i-1
        while temp < list_of_numbers[j] and j >=0:
            ##while loop is there to swap elements in case we find a value smaller than the one at index i
            ## this will only continue till j is at 0, since index cant be negative
            ##we use j to access values is that i keeps moving forward, where as j is moving back
            list_of_numbers[j+1] = list_of_numbers[j]
            list_of_numbers[j] = temp
            j-=1
    return list_of_numbers

def merge(list1, list2):
    combined = [] ##initiating list which will be sorted
    i = 0 ##pointers of the sub-list
    j = 0
    while i < len(list1) and j < len(list2):
        ##cant use for loop for comparison between 2 seperate lists
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i+=1
        else:
            combined.append(list2[j])
            j+=1
    while i < len(list1):
        ##this while loop is there to add elements for list1 if there are any left to be added to the combined list
        ##we donot need to compare them as the sub-lists are assumed to have been sorted
        combined.append(list1[i])
        i+=1
    while j < len(list2):
        combined.append(list2[j])
        j+=1
    return combined

def merge_sort(list_of_numbers):
    if len(list_of_numbers) == 1:
        return list_of_numbers
    mid = int(len(list_of_numbers)/2) ##finding the midpoint of unsorted full list, using int for odd numbered lenght
    left = list_of_numbers[:mid] ##starting from 0 till but not including mid index
    right = list_of_numbers[mid:] ## from mid index till last
    ##since left and right are not sorted we cannot input them into merge function
    ##so we use recursion to break left and right again and again till we get only 1 item in a list
    ##then these seperate elements are combined to give 2 sorted sub-lists
    return (merge(merge_sort(left), merge_sort(right)))
    ##this return statement above will first keep breaking the original "left" in the list
    ## and keeps combining them, once the left list is sorted completely - [13,55,99,102] it moves
    ## to the "right" list and begins the same there


listofnumber = [99,102,13,55,1,78,999,23,37]
print(merge_sort(listofnumber))



        