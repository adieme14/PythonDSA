""" LeetCode Problem: 242. Valid Anagram
    Solution 1: Sort both strings and compare them.
    Time Complexity: O(n log n) where n is the length of the strings.
    Space Complexity: O(n) for storing the sorted strings."""

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)


""" Solution 2: Use a dictionary to count character frequencies.
    Time Complexity: O(n) where n is the length of the strings.
    Space Complexity: O(k) where k is the number of unique characters."""

def is_anagram_v2(str1, str2):
    if len(str1) != len(str2):
        return False
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Count character frequencies
    char_map = {}
    for char in str1:
        char_map[char] = char_map.get(char, 0) + 1

    # Decrease counts for characters in the second string
    for c in str2:
        char_map[c] = char_map.get(c, 0) - 1 
        # Decrement for chars in t
        if char_map[c] < 0:
            return False
    
    return True

""" Solution 3: Use an array to count character frequencies for lowercase English letters.
    Time Complexity: O(n) where n is the length of the strings.
    Space Complexity: O(1) since the size of the frequency array is constant (26)."""

def isAnagram_v3(s: str, t: str) -> bool:
    # Step 1: Anagrams must be the exact same length
    if len(s) != len(t):
        # If lengths differ, they cannot be anagrams
        return False
    
    # Step 2: Create a frequency tracker array for 26 lowercase English letters
    count = [0] * 26
    
    # Step 3: Increment for string s and decrement for string t
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
        
    # Step 4: Verify if all character frequencies balanced out to zero
    for num in count:
        if num != 0:
            # A non-zero value means a character mismatch
            return False
            
    return True


if __name__ == "__main__":
    print(isAnagram_v3("aab", "aba"))  # True
    print(is_anagram("hello", "world"))    # False