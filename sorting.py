def bubble(list):
    for i in range(len(list) - 1):
        for sort in range(len(list) - 1):
            if list[sort] > list[sort + 1]:
                temp = list[sort]
                list[sort] = list[sort + 1]
                list[sort + 1] = temp
        sort = 0
    return list

def selection(list):
    #Iterate over the list
    for sorted in range(len(list)-1):
        minimum = sorted
        #find the smallest value in the unsorted portion of the list
        for check in range(sorted + 1, len(list)):
            if list[minimum] > list[check]:
                minimum = check

        #swap the smallest value found with the first unsorted value of the list
        temp = list[minimum]
        list[minimum] = list[sorted]
        list[sorted] = temp
    
    return list



def insertion(list):
    #iterate over the list started at the 2nd element
    for sorted in range(1, len(list) ):
        check = sorted
        #Check to see if the element on front of the sorted list is less than the element at the end of the sorted list
        #Then insert that element into the correct spot in the list
        while (list[check] < list[check - 1]) and (check > 0):    
            #Swap the two elements if the rightmost one is smaller
            temp = list[check]
            list[check] = list[check - 1]
            list[check - 1] = temp
            check -= 1

    return list
