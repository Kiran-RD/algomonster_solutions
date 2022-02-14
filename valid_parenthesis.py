def valid_parentheses(s: str) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    stack = []
    pairs = {')':'(', '}':'{', ']':'['}
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if i in pairs:
                if stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
    return True if not stack else False
            
if __name__ == '__main__':
    s = input()
    res = valid_parentheses(s)
    print('true' if res else 'false')