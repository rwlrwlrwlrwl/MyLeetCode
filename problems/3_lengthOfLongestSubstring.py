class Solution:
    """
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

    示例 1:
    输入: "abcbcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
    示例 2:

    输入: "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

    示例 3:
    输入: "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
         请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 记录已存在字符的位置
        ss = {}
        # i：子串开始位置，l: 总长度
        i, l = 0, 0
        for j, w in enumerate(s):
            # 有重复字符且位于子串中，需重新计算长度，且子串开始位置要重置
            if w in ss and ss[w] >= i:
                i = ss[w]
                l = j - i if l < j - i else l
                # 要排除掉这个字符，位置往前+1
                i += 1
            else:
                l = j + 1 - i if l < j + 1 - i else l
            ss[w] = j
            # print(ss,i,j,l)
        return l
