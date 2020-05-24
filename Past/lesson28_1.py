# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be 1pm positive integer.
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

# Examples:
# s = "3[1pm]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


def decodeString(s):
    stack = ['']
    for c in s:
        if c.isdigit() and not (stack and stack[-1].isdigit()):
            stack.append(c)
        elif c == '[':
            stack.append('')
        elif c == ']':
            seq = stack.pop()
            k = int(stack.pop())
            stack[-1] += seq * k
        else:
            stack[-1] += c
        print(stack)
    return ''.join(stack)

s = "3[a2[c]]"
print(decodeString(s))