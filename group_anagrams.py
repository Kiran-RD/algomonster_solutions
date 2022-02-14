from typing import List

def group_anagrams(strings: List[str]) -> List[List[str]]:
    n = len(strings)
    anagrams_map = []
    for word in strings:
        word_set = set(word)
        if word_set in anagrams_map:
            anagrams_map[word_set].append(word)
        else:
            anagrams_map[word_set] = [word]            

    return anagrams_map.items()

if __name__ == '__main__':
    strings = input().split()
    res = group_anagrams(strings)
    for row in res:
        row.sort()
    res.sort(key=lambda row: row[0])
    for row in res:
        print(' '.join(row))
