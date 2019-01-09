
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        chars = set()
        res = 0
        while left < len(s) and right < len(s):
            if s[right] in chars:
                #if s[left] in chars:
                chars.remove(s[left])
                left += 1
            else:
                chars.add(s[right])
                right += 1
                res = max(res, len(chars))
        return res



if __name__ == "__main__":
    object = Solution()
    a = object.lengthOfLongestSubstring("abcdbacbdebcbb")
    print (a)
