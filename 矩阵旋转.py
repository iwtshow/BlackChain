
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

import copy
# def rotate( matrix):
#     result = copy.deepcopy(matrix)
#     nums = len(matrix)
#     for i in range(nums):
#         for j in range(nums):
#             a = matrix[nums-i-1][j]
#             result[j][i] = a
#     return result
#


def rotate(self,matrix):
    result = []
    nums = len(matrix)
    for y in range(nums):
        result.append([])
        for x in range(nums):
            result[y].append([])
    for i in range(nums):
        for j in range(nums):
            n = matrix[nums - i - 1][j]
            result[j][i] = n
    return result

print(rotate(matrix))
