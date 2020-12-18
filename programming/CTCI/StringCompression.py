def stringToCompress(string: str):
    x = {}
    for i in string:
        if i in x.keys():
            x[i] += 1
        else:
            x[i] = 1

    compressed_str = "".join('{}{}'.format(key, value) for key, value in x.items())
    if len(compressed_str) > len(string):
        return string
    else:
        return compressed_str

print(stringToCompress("tissoooot"))
