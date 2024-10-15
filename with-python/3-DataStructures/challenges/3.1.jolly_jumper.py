# A sequence of n > 0 integers is called a jolly jumper if 
# the absolute values of the differences between successive elements 
# take on all possible values 1 through n - 1.

def is_jolly_jumper(nums):
    n = len(nums)
    if n == 1:
        return True

    diffs = [False] * n

    for i in range(n - 1):
        diff = abs(nums[i + 1] - nums[i])
        
        # check out of range and duplication 
        if diff == 0 or diff > n - 1 or diffs[diff]:
            return False
        
        diffs[diff] = True

    return True

def main():
    inputs = [
        [1, 4, 2, 3], # 3 2 1 -> jolly
        [5, 1, 4, 2, -1, 6] # 4 3 2 3 5 -> not jolly (lack 1)
    ]

    for nums in inputs:
        print(f"{'Jolly' if is_jolly_jumper(nums) else 'Not Jolly'}: {nums}")

if __name__ == '__main__':
    main()