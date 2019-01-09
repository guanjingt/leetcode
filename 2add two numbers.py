import numpy as np


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        tmp = ListNode(0)
        res = tmp   
        flag = 0
        while l1 or l2:
            tmpsum = 0
            if l1:
                tmpsum = l1.val
                l1 = l1.next
            if l2:
                tmpsum += l2.val
                l2 = l2.next
            tmpres = ((tmpsum + flag) % 10)
            flag = ((tmpsum + flag) // 10)
            res.next = ListNode(tmpres)
            res = res.next
        if flag:
            res.next = ListNode(1)
        res = tmp.next
        del tmp
        return res


if __name__ == "__main__":

    #a = [2,4,3]
    #b = [5,6,4]
    l1_1 = ListNode(2)
    l1_2 = ListNode(4)
    l1_3 = ListNode(3)
    l1_1.next = l1_2
    l1_2.next = l1_3

    l2_1 = ListNode(5)
    l2_2 = ListNode(6)
    l2_3 = ListNode(4)
    l2_1.next = l2_2
    l2_2.next = l2_3

    l3_1 = Solution().addTwoNumbers(l1_1,l2_1)

    while l3_1 != None:
        print(l3_1.val)
        l3_1 = l3_1.next





















"""
class Solution(object):
    def twoSum(self, nums, target):
        nums_dict = {}
        for i, num in enumerate(nums):
            print (num)
            #print (i)
            if num in nums_dict:
                print (nums_dict)
                return [nums_dict[num], i]
            else:
                nums_dict[target - num] = i





if __name__ == "__main__":
    nums = [2,2,3,7,4]
    target = 6
    object = Solution()
    print (object.twoSum(nums, target))

"""




















"""
class Two_Sum(object):

    def __init__(self):
        self.map = {0:2, 1:7, 2:11, 3:15}
        self.target =9



    def get_value(self, d):
        for k, v in self.map.items():
            if v == d:
                return k


    def Solution(self):
        length = len(self.map)
        num1 = 0

        for i in range(length):
            num = self.target - self.map.get(i)
            num1 = self.get_value(num)
            return i, num1

    def run(self):
        print (self.Solution())


if __name__ == '__main__':
    object1 = Two_Sum()
    object1.run()
"""
