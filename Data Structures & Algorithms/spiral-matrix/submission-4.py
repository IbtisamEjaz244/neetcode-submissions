class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse the top row: left -> right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # Traverse the right column: top -> bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # Traverse the bottom row: right -> left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # Traverse the left column: bottom -> top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result