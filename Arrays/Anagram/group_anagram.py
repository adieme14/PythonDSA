
from collections import defaultdict

""" leetcode 49: Group Anagrams
    Solution 1: Groups anagrams from a list of strings.
    Time Complexity: O(n * k log k) where n is the number of strings and k is the maximum length of a string.
    Space Complexity: O(n * k) for storing the grouped anagrams."""

def group_anagrams(strs):
    anagram_groups = defaultdict(list)
    
    for word in strs:
        # Sort the word to create a unique key for each anagram group
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)
        
    return list(anagram_groups.values())

""" Solution 1.a: Same as above but using a regular dictionary instead of defaultdict."""
def groupAnagrams(strs):
    groups = {}

    for word in strs:
        key = ''.join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())

""" Solution 2: Groups anagrams using character count as a key.
    Time Complexity: O(n * k) where n is the number of strings and k is the maximum length of a string.
    Space Complexity: O(n * k) for storing the grouped anagrams."""

def group_anagrams_v2(strs):
    anagram_groups = defaultdict(list)

    for word in strs:
        # Create a character count tuple as the key
        char_count = [0] * 26  # Assuming only lowercase letters
        
        for c in word:
            char_count[ord(c) - ord('a')] += 1
            
        key = tuple(char_count)
        anagram_groups[key].append(word)

    return list(anagram_groups.values())


""" Solution 2.a: Same as above but using a regular dictionary instead of defaultdict."""

def groupAnagramsV2(strs):
    groups = {}

    for word in strs:
        char_count = [0] * 26
        
        for c in word:
            char_count[ord(c) - ord('a')] += 1
            
        key = tuple(char_count)

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    print(groupAnagramsV2(strs))