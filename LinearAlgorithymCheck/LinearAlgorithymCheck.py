
list = [14,19,23,28,31,39,43,47]
print(list)
SearchValue = int(input("Please enter a number: "))

#
#
#

for i in range (0, (len(list))):
    if list[i] == SearchValue:
        position = i+1
        print("Found at list position: ", + position)
        break
    elif i == len(list)-1:
        print("Item not found in list")
        break
 

#Linear search is a very simple search algorithm. In this type of search, a sequential search is made over all items one by one. 
#Every item is checked and if a match is found then that particular item is returned, otherwise the search continues till the end of the data collection.