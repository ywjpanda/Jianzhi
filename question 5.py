'''
剑指 Offer 05. 替换空格

请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例1
输入：s = "We are happy."
输出："We%20are%20happy."

限制：
0 <= s 的长度 <= 10000

start from nothing:
class Solution:
    def replaceSpace(self, s: str) -> str:
'''

# '''
# # 解法 1
# 创建一个新str
# 在空格处添加%20
# 剩下的加后面
# 时间：O(N)
# 空间：O(N)
# '''
# class Solution:
#     def replaceSpace(self, s: str) -> str:
#         s_new = ""
#         for c in s:
#             if c == " ":
#                 s_new = s_new + "%20"
#             else:
#                 s_new = s_new + c
#         return s_new

'''
# 解法 2
直接更改
'''
class Solution:
    def replaceSpace(self, s: str) -> str:


        return s.replace(" ","%20")


if __name__ == '__main__':
    s_input = "We are happy."
    s_targe  = "We%20are%20happy."
    ss = Solution()
    s_output = ss.replaceSpace( s_input)
    print("output is: ",s_output)
    print("结果正确吗？", s_output == s_targe)