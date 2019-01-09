class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        tem2 = str(x)
        tem = list(tem2)
        length = len(tem)
        if tem[0] == '-':
            for i,j in zip(range(length-1,1,-1), range(1,length//2+1,1)):
                tem[i], tem[j] = tem[j], tem[i]

        else:
            for i,j in zip(range(length-1,0,-1), range(length//2)):
                tem[i], tem[j] = tem[j], tem[i]
        print (str("".join(tem)))
        result = int(str("".join(tem)))
        print (result)
        if result > 2**31:
            return 0

        if result < -2**31+1:
            return 0

        return result

    def run(self):
        test = 15300
        result = self.reverse(test)
        print (result)


if __name__ == '__main__':
    object = Solution()
    object.run()





