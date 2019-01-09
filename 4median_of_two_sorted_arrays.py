import math



class Solution:
    # @return a float
    # @line20 must multiply 0.5 for return a float else it will return an int
    def getKth(self, A, B, k):
        lenA = len(A)
        lenB = len(B)

        if lenA > lenB: return self.getKth(B, A, k)
        if lenA == 0: return B[k - 1]
        if k == 1: return min(A[0], B[0])
        pa = math.floor(min(k/2, lenA)); pb = math.floor(k - pa)
        if A[pa - 1] < B[pb - 1]:
            return self.getKth(A[pa:], B, pb)
        elif A[pa - 1] > B[pb - 1]:
            return self.getKth(A, B[pb:], pa)
        else:
            return A[pa-1]


    def findMedianSortedArrays(self, A, B):
        lenA = len(A); lenB = len(B)
        if (lenA + lenB) % 2 == 1:
            return self.getKth(A, B, (lenA + lenB+1)/2)
        else:
            return (self.getKth(A, B, (lenA + lenB)/2) + self.getKth(A, B, (lenA + lenB)/2 + 1)) * 0.5


if __name__ == '__main__':

    A = [1,2,6,9]
    B = [3,4,7,8]
    object = Solution()

    a = object.findMedianSortedArrays(A,B)
    print (a)
