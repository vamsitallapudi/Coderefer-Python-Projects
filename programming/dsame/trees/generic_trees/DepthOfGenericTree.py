def depth_of_generic_tree(arr: list):
    currDepth, maxDepth = 0, 0
    for i in range(0, len(arr)):
        currDepth, j = 0, i
        while arr[j] != -1:
            currDepth += 1
            j = arr[j]
        if currDepth > maxDepth:
            maxDepth = currDepth

    return maxDepth


print(depth_of_generic_tree([-1, 0, 1, 6, 6, 0, 0, 2, 7]))
