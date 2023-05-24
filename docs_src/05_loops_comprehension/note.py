# Iterable, Iterator, and Generator

nums = [1, 2, 3, 4, 5]

# def double_nums(nums):
#     output = []
#     for num in nums:
#         output.append(num*2)
#     return output
#
# output_nums = double_nums(nums)
# print(output_nums)

def double_nums(nums):
    for num in nums:
        yield num*2
output_nums = double_nums(nums)
print(list(output_nums))
