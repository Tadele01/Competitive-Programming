class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        move = 0
        for i in range(1, len(A)):
            if A[i-1] == A[i]:
                A[i] +=1
                move +=1
            elif A[i-1] > A[i]:
                diff = A[i-1] - A[i]
                A[i] += diff + 1
                move += diff + 1
        return move