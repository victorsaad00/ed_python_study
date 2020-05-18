####################################
########### Bubble Sort: ###########
####################################
def bubble_sort(bubble_list):
    print('Bubble Sort')
    print(bubble_list)
    for i in range(1,len(bubble_list)):
        for j in range(0,len(bubble_list)-1):
            if bubble_list[j] > bubble_list[j + 1]:
                element = bubble_list[j + 1]
                bubble_list[j+1] = bubble_list[j]
                bubble_list[j] = element

    print(bubble_list)


####################################
######### Insertion Sort: ##########
####################################
def insertion_sort(insList):
    print('Insertion Sort')
    print(insList)
    for i in range(1, len(insList)-1):
        key = i
        while key > 0 and insList[key - 1] > insList[key]:
            element = insList[key]
            insList[key] = insList[key - 1]
            insList[key - 1] = element
            key = key - 1

    print(insList)
####################################
####################################


####################################
######### Selection Sort ###########
####################################
def selection_sort(secList):
    print('Selection Sort')
    print(secList)
    length = len(secList)
    for j in range(0, length - 1):
        iMin = j

        for i in range(j+1, length):
            if secList[i] < secList[iMin]:
                iMin = i
        
        if iMin != j:
            element = secList[j]
            secList[j] = secList[iMin]
            secList[iMin] = element

    print(secList)
####################################
####################################


###################################
########### Merge Sort ############
###################################
def merge_sort(mList):
    if len(mList) > 1:
        mid = len(mList)//2
        L = mList[:mid]
        R = mList[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                mList[k] = L[i] 
                i+=1
            else: 
                mList[k] = R[j] 
                j+=1
            k+=1
        
        while i < len(L): 
            mList[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            mList[k] = R[j] 
            j+=1
            k+=1
    
list = [9,8,5,4,3,1,2,6,7]
print(list)
merge_sort(list)
print(list)
####################################
####################################
