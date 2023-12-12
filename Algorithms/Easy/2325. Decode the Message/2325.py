class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alph = "abcdefghijklmnopqrstuvwxyz"
        cipher, idx = { ' ' : ' ' }, 0
        for ch in key:
            if ch not in cipher:
                cipher[ch] = alph[idx]
                idx += 1
        return ''.join(map(lambda x: cipher[x], message))

# first, we can create a dictionary to map each character in the key to a character in the alphabet
# then, we can iterate through the message
# for each character, we can map to the corresponding character from the dictionary