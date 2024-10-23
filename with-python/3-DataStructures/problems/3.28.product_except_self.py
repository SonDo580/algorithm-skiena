# You have an unordered array X of n integers.
# Find the array M containing n elements where Mi
# is the product of all integers in X except for Xi.
# You may not use division. You can use extra memory


def product_except_self(nums):
    n = len(nums)
    products = []

    prefix_product = 1
    for i in range(n):
        products.append(prefix_product)
        prefix_product *= nums[i]

    suffix_product = 1
    for i in range(n - 1, -1, -1):
        products[i] *= suffix_product
        suffix_product *= nums[i]

    return products


def product_except_self_1(nums):
    # Another approach: add zero checking

    n = len(nums)
    products = []

    count_zero = 0
    zero_index = -1
    non_zero_product = 1

    prefix_product = 1
    for i in range(n):
        if nums[i] == 0:
            count_zero += 1
            if count_zero == 2:
                return [0] * n
            zero_index = i
        else:
            non_zero_product *= nums[i]

        products.append(prefix_product)
        prefix_product *= nums[i]

    if count_zero == 1:
        products = [0] * n
        products[zero_index] = non_zero_product
        return products

    suffix_product = 1
    for i in range(n - 1, -1, -1):
        products[i] *= suffix_product
        suffix_product *= nums[i]

    return products


def main():
    inputs = [[1, 2, 3, 4], [1, 0, 3, 4], [1, 0, 3, 0]]

    outputs = []
    for input in inputs:
        outputs.append(product_except_self(input))

    assert outputs == [
        [24, 12, 8, 6],
        [0, 12, 0, 0],
        [0, 0, 0, 0],
    ]


if __name__ == "__main__":
    main()
