# python3
def max_pairwise_product(numbers):
    x = sorted(numbers)
    n = len(numbers)
    return x[n-1] * x[n-2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
