
string = "((()))())()()()()))("

stack = []
last_invalid = -1  # Pointer to the last invalid parenthesis
max_len = 0

for i, char in enumerate(string):
    if char == "(":
        stack.append(i)
    else:
        if stack:
            stack.pop()
            #therefore, i is matched
            if not stack:
                max_len = max(max_len, i - last_invalid)
            else:
                max_len = max(max_len, i - stack[-1])
        else:
            last_invalid = i

print(max_len)




