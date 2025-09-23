class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Create a dictionary to count the frequency of each character
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        # Iterate through the string to find the first unique character
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i

        # Return -1 if there is no unique character
        return -1