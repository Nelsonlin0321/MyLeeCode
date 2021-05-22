# https://leetcode.com/problems/search-a-2d-matrix-ii/submissions/
# Runtime: 168 ms, faster than 40.12% of Python3 online submissions for Search a 2D Matrix II.
# Memory Usage: 20.7 MB, less than 27.40% of Python3 online submissions for Search a 2D Matrix II.

class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        hight = len(matrix) - 1
        width = len(matrix[0]) - 1
        hi = 0
        wi = width

        while 0 <= hi <= hight and 0 <= wi <= width:

            pivot = matrix[hi][wi]
            if pivot == target:
                return True
            elif pivot < target:  # 该位置小于 target
                hi += 1  # 高度得加一
                wi = len(matrix[0]) - 1  # 同时宽度重置
            elif pivot > target:  # 该位置大于target，我们不要能加高度，只能降低宽度
                wi -= 1

        return False

# Runtime: 152 ms, faster than 97.47% of Python3 online submissions for Search a 2D Matrix II.
# Memory Usage: 20.5 MB, less than 64.52% of Python3 online submissions for Search a 2D Matrix II.

class Solution:

    def binary_search(self, arr, target) -> bool:
        lo = 0
        hi = len(arr) - 1

        while (hi - lo) > 1:  # to be disuss
            mid = lo + (hi - lo) // 2

            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                hi = mid
            elif arr[mid] < target:
                lo = mid
        if arr[hi] == target or arr[lo] == target:
            return True
        else:
            return False

    def searchMatrix(self, matrix, target) -> bool:
        hight = len(matrix) - 1
        width = len(matrix[0]) - 1
        hi = 0
        wi = width

        while 0 <= hi <= hight:  # 对每一行进行二分查找

            pivot = matrix[hi][wi]
            if pivot == target:
                return True
            elif target > pivot:  # target 大于目前的该位置的数，因为width 已经是最大了，所以我们宽度要加一
                hi += 1  # 高度得加一
                # wi = len(matrix[0]) - 1  # 同时宽度重置
            elif target < pivot:  # target 小于目前的该位置的数，已经不能加加高度了， 只能在该列中查找先。
                is_found = self.binary_search(matrix[hi], target)
                if is_found:
                    return True
                else:
                    hi += 1  # 得在下一列中查找

        return False


if __name__ == "__main__":
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 20
    print(Solution().searchMatrix(matrix, target))
    # arr = [10, 13, 14, 17, 24]
    # target = 13
    # print(binary_search(arr, target))
