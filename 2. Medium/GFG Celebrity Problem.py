class Solution:
    def celebrity(self, mat):
        # code here
        n = len(mat)
        i, j = 0, n - 1

        # mat[i][j] means i knows j
        while i < j:
            if mat[i][j] == 1:
                # it means i knows j, i can't be celebrity
                i += 1
            else:  # mat[i][j] == 0:
                # it means i doesn't know j, j can't be celebrity
                j -= 1

        candidate = i  # or j since loop terminates will terminate at i==j

        for k in range(n):
            if candidate != k:
                # check if candidate knows k or k doesn't know candidate, if either is true, candidate can't be celebrity
                if mat[candidate][k] == 1 or mat[k][candidate] == 0:
                    return -1
        return candidate
