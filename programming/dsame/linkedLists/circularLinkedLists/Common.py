
def print_and_iterate(current):
    if not current:
        return None
    print("{}".format(current.data), end=" ")
    current = current.next
    return current