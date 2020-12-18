from array import array

intarray = array('I', (0 for i in range(0, 5)))
for i in range(0, len(intarray)):
    intarray[i] = i

"""deleting from the end of an array"""


def delete_end_of_array():
    length = len(intarray)
    length -= 1  # we are not actually freeing the item. we're just reducing count by 1
    for i in range(0, length):  # using declared length instead of len(intarray)
        print(i)


def delete_start_of_array():
    length = len(intarray)
    for i in range(1, length):
        intarray[i - 1] = intarray[i]

    print(intarray)

def delete_from_anywhere(index:int):
    length = len(intarray)
    for i in range(index+1, length):
        intarray[i-1] = intarray[i]
    length-=1
    for i in range(0, length):  # using declared length instead of len(intarray)
        print(intarray[i])


# delete_end_of_array()
# delete_start_of_array()
delete_from_anywhere(2)