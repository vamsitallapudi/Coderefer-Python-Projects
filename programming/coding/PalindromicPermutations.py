from array import array

# to check if more than one char is odd
def check_more_than_one_odd(lst):
    odd_found = False
    for i in lst:
        if i % 2 == 1:
            if odd_found:
                return False
            odd_found = True
    return True


# map each character to a number a->0, b->1, z->25
def map_char_to_num(c):
    a = ord('a')
    z = ord('z')
    s = ord(c)
    if a <= s <= z:
        return s - a
    else:
        return -1

# store each char in array
def store_chars(lst):
    my_arr = array('I', (0 for i in range(ord('z') - ord('a') + 1 )))
    for i in lst:
        x = map_char_to_num(i)
        if(x > -1):
            my_arr[x] = my_arr[x]+1

    return my_arr

# process the given string
def process_str(str):
    lst = list(str)
    arr = store_chars(lst)
    if check_more_than_one_odd(arr):
        print('True')
    else:
        print('False')

x = input('Enter a String:')
process_str(x)