from array import array

intarray = array('I', (0 for i in range(0, 5)))


def insert_end_of_array():
    length = 0

    for i in range(0, 3):
        intarray[length] = i
        length += 1
    intarray[length] = 10
    length += 1
    print(intarray)


def insert_start_of_array():
    # time complexity - O(N) since each element has to be shifted to right to accommodate space.
    for i in range(2, -1, -1):
        intarray[i + 1] = intarray[i]
    intarray[0] = 4
    print(intarray)


def insert_at_index(index: int, ele: int):
    n = len(intarray)
    for i in range(n - 1, index - 1, -1):
        intarray[i] = intarray[i-1]
    intarray[index] = ele
    print(intarray)


# insert_end_of_array()
# insert_start_of_array()
# print(intarray)
insert_at_index(4, 10)
