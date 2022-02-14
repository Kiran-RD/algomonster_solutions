def is_isomorphic(str_1: str, str_2: str) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    if len(str_1) == len(str_2):
        isomorohic = {}
        used = set()
        n = len(str_1)
        for i in range(n):
            if str_2[i] in isomorohic:
                if isomorohic[str_2[i]] != str_1[i]:
                    return False

            else:
                if str_1[i] in used:
                    return False
                isomorohic[str_2[i]] = str_1[i]
                used.add(str_1[i])
        return True
    else:
        return False

if __name__ == '__main__':
    str_1 = input()
    str_2 = input()
    res = is_isomorphic(str_1, str_2)
    print('true' if res else 'false')