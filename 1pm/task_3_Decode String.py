# The encoding rule is: k[encoded_string],
# where the encoded_string inside the square brackets is being repeated exactly k times.
# Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces,
# square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
# For example, there won't be input like 3a or 2[4].

# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".





def get_char():
    res = ""
    while stack and not stack[-1] == '[':
        res = stack.pop() + res
    return res

def get_num():
    num = ""
    while stack and stack[-1].isdigit():
        num = stack.pop() + num
    return num

s="2[ab2[cc]b]"
final = ""
stack = []
for ele in s:
    if ele == "]":  # pop routine
        res = get_char()
        stack.pop()  # removing the "[" bracket
        num = get_num()
        if num:
            res = int(num) * res
        if stack == []:
            final += res
        else:
            stack.append(res)
    else:
        stack.append(ele)
if stack:
    final += ''.join(stack)

print(final)


